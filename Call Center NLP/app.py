# Streamlit Dashboard - Call Center NLP
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import spacy
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from transformers import pipeline
from keybert import KeyBERT
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

# Page config
st.set_page_config(
    page_title="Call Center NLP Dashboard",
    page_icon="📞",
    layout="wide"
)

# ─── LOAD MODELS 

@st.cache_resource
def load_spacy():
    return spacy.load('en_core_web_sm')

@st.cache_resource
def load_sentiment_model():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

@st.cache_resource
def load_summarizer():
    return pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )

@st.cache_resource
def load_topic_classifier():
    return pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli"
    )

@st.cache_resource
def load_keybert():
    return KeyBERT()

@st.cache_resource
def load_qa_pipeline():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

@st.cache_data
def load_data():
    return pd.read_csv('processed_calls.csv')

# ─── BUILD RAG FROM CSV 

@st.cache_resource
def build_rag_from_csv():
    """
    Builds a ChromaDB vector store in-memory from processed_calls.csv.
    Runs once on first load, cached for the session.
    """
    df = pd.read_csv('processed_calls.csv')

    # Build LangChain Document objects from each transcript row
    docs = []
    for _, row in df.iterrows():
        content = str(row.get('Transcript', ''))
        metadata = {
            'customer': str(row.get('Name', 'Unknown')),
            'type':     str(row.get('Type', 'Unknown')),
            'sentiment':str(row.get('Sentiment', 'Unknown')),
            'summary':  str(row.get('Summary', ''))
        }
        docs.append(Document(page_content=content, metadata=metadata))

    # Embed and store in-memory ChromaDB (no persist_directory)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings
        
    )
    return vectordb

#  HEADER 

st.title("📞 Call Center NLP Dashboard")
st.markdown("**End-to-end NLP pipeline for call center transcript analysis**")
st.markdown("---")

#  SIDEBAR 

st.sidebar.title("Navigation")
tab_selection = st.sidebar.radio(
    "Choose a section:",
    [
        "📊 Overview & EDA",
        "🔍 Analyze a Call",
        "🤖 RAG Assistant",
        "🗂️ Cluster Explorer"
    ]
)

#  OVERVIEW & EDA 

if tab_selection == "📊 Overview & EDA":
    st.header("📊 Dataset Overview")
    df = load_data()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Calls", len(df))
    col2.metric("Call Types", df['Type'].nunique())
    col3.metric("Sentiment Types", df['Sentiment'].nunique())
    col4.metric(
        "Avg Words/Call",
        f"{df['Transcript'].apply(lambda x: len(str(x).split())).mean():.0f}"
    )

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sentiment Distribution")
        sentiment_counts = df['Sentiment'].value_counts()
        fig, ax = plt.subplots()
        ax.bar(
            sentiment_counts.index,
            sentiment_counts.values,
            color=['green', 'blue', 'red', 'orange', 'purple']
        )
        ax.set_xlabel("Sentiment")
        ax.set_ylabel("Count")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with col2:
        st.subheader("Call Type Distribution")
        type_counts = df['Type'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%')
        st.pyplot(fig)

    st.markdown("---")
    st.subheader("Raw Data")
    st.dataframe(
        df[['Name', 'Type', 'Sentiment',
            'Predicted_Topic', 'Predicted_Intent', 'Summary']]
        .style.highlight_max(axis=0)
    )

# ANALYZE A SINGLE CALL

elif tab_selection == "🔍 Analyze a Call":
    st.header("🔍 Analyze a Single Transcript")
    st.markdown("Paste any call transcript below to run the full NLP pipeline on it.")

    nlp              = load_spacy()
    sentiment_model  = load_sentiment_model()
    summarizer       = load_summarizer()
    topic_classifier = load_topic_classifier()
    kw_model         = load_keybert()

    user_transcript = st.text_area(
        "Paste transcript here:",
        height=200,
        placeholder="Hello, I'm calling about my order..."
    )

    if st.button("🚀 Analyze", type="primary"):
        if user_transcript.strip() == "":
            st.warning("Please enter a transcript first.")
        else:
            st.markdown("---")
            with st.spinner("Running NLP pipeline..."):

                # 1. PII Redaction
                doc = nlp(user_transcript)
                redacted = user_transcript
                for ent in doc.ents:
                    if ent.label_ in ['PERSON']:
                        redacted = redacted.replace(ent.text, '[CUSTOMER_NAME]')
                redacted = re.sub(r'\b\d{6}\b', '[ORDER_NUMBER]', redacted)

                # 2. Sentiment
                sentiment_result = sentiment_model(user_transcript[:512])[0]

                # 3. Summarization
                if len(user_transcript.split()) > 30:
                    summary_result = summarizer(
                        user_transcript[:1024],
                        max_length=60,
                        min_length=20,
                        do_sample=False
                    )[0]['summary_text']
                else:
                    summary_result = "Transcript too short to summarize."

                # 4. Topic (zero-shot)
                topic_labels = [
                    'product inquiry', 'complaint',
                    'technical issue', 'compliment', 'order placement'
                ]
                topic_result = topic_classifier(
                    user_transcript[:512],
                    candidate_labels=topic_labels
                )['labels'][0]

                # 5. Intent (zero-shot)
                intent_labels = [
                    'get information', 'file a complaint',
                    'request refund', 'cancel order',
                    'get technical support', 'give positive feedback'
                ]
                intent_result = topic_classifier(
                    user_transcript[:512],
                    candidate_labels=intent_labels
                )['labels'][0]

                # 6. Keywords
                keywords    = kw_model.extract_keywords(
                    user_transcript,
                    keyphrase_ngram_range=(1, 2),
                    stop_words='english',
                    top_n=5
                )
                keyword_list = [kw[0] for kw in keywords]

            # Display results
            col1, col2, col3 = st.columns(3)
            col1.metric("Sentiment", sentiment_result['label'])
            col2.metric("Topic",     topic_result.title())
            col3.metric("Intent",    intent_result.title())

            st.markdown("---")
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📝 Summary")
                st.info(summary_result)

                st.subheader("🔑 Keywords")
                for kw in keyword_list:
                    st.badge(kw)

            with col2:
                st.subheader("🔒 PII Redacted Version")
                st.success(redacted)

                st.subheader("🏷️ Named Entities Found")
                for ent in doc.ents:
                    st.write(f"**{ent.text}** → {ent.label_}")

#  RAG ASSISTANT

elif tab_selection == "🤖 RAG Assistant":
    st.header("🤖 RAG Assistant")
    st.markdown("Ask any question about your call center data.")

    with st.spinner("Building vector store from transcripts... (first load only)"):
        vectordb   = build_rag_from_csv()

    qa_pipeline = load_qa_pipeline()

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Suggested questions
    st.subheader("💡 Try these questions:")
    col1, col2, col3 = st.columns(3)
    if col1.button("What are common complaints?"):
        st.session_state.current_q = "What are common complaints?"
    if col2.button("Which customers are angry?"):
        st.session_state.current_q = "Which customers are angry?"
    if col3.button("What products are mentioned?"):
        st.session_state.current_q = "What products are mentioned?"

    question = st.text_input(
        "Or type your own question:",
        value=st.session_state.get('current_q', '')
    )

    if st.button("Ask 🔍"):
        if question:
            with st.spinner("Searching transcripts..."):
                relevant_docs = vectordb.similarity_search(question, k=3)
                context = "\n\n".join([doc.page_content for doc in relevant_docs])

                prompt = f"""Based on call center transcripts, answer briefly.
Context: {context[:800]}
Question: {question}
Answer:"""
                answer = qa_pipeline(
                    prompt, max_length=100, do_sample=False
                )[0]['generated_text']

                st.session_state.chat_history.append({
                    'question': question,
                    'answer':   answer,
                    'sources': [
                        f"{d.metadata['customer']} ({d.metadata['type']})"
                        for d in relevant_docs
                    ]
                })

    for chat in reversed(st.session_state.chat_history):
        with st.container():
            st.markdown(f"**Q:** {chat['question']}")
            st.markdown(f"**A:** {chat['answer']}")
            st.caption(f"Sources: {', '.join(chat['sources'])}")
            st.markdown("---")

# CLUSTER EXPLORER 

elif tab_selection == "🗂️ Cluster Explorer":
    st.header("🗂️ Customer Cluster Explorer")
    df = load_data()

    vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
    X          = vectorizer.fit_transform(df['Transcript'])
    kmeans     = KMeans(n_clusters=5, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(X)
    pca        = PCA(n_components=2)
    X_2d       = pca.fit_transform(X.toarray())

    st.subheader("Customer Call Clusters (PCA Visualization)")
    colors = ['red', 'blue', 'green', 'orange', 'purple']
    fig, ax = plt.subplots(figsize=(10, 6))
    for cluster in range(5):
        mask = df['Cluster'] == cluster
        ax.scatter(
            X_2d[mask, 0], X_2d[mask, 1],
            c=colors[cluster], label=f'Cluster {cluster}', s=100
        )
        for idx in df[mask].index:
            ax.annotate(
                df['Name'][idx].split()[0],
                (X_2d[idx, 0], X_2d[idx, 1]),
                fontsize=8
            )
    ax.legend()
    ax.set_xlabel("PCA Component 1")
    ax.set_ylabel("PCA Component 2")
    st.pyplot(fig)

    st.markdown("---")
    selected_cluster = st.selectbox(
        "Select a cluster to explore:",
        options=[0, 1, 2, 3, 4],
        format_func=lambda x: f"Cluster {x}"
    )
    cluster_df = df[df['Cluster'] == selected_cluster]
    st.subheader(f"Cluster {selected_cluster} — {len(cluster_df)} calls")
    st.dataframe(
        cluster_df[['Name', 'Type', 'Sentiment', 'Predicted_Topic', 'Summary']]
    )
