# questions.py
from utils import format_documents
from file_processing import search_documents

class QuestionContext:
    def __init__(self, index, documents, llm_chain, model_name, repo_name, github_url, conversation_history, file_type_counts, filenames):
        self.index = index
        self.documents = documents
        self.llm_chain = llm_chain
        self.model_name = model_name
        self.repo_name = repo_name
        self.github_url = github_url
        self.conversation_history = conversation_history
        self.file_type_counts = file_type_counts
        self.filenames = filenames

def ask_question(question, context: QuestionContext):
    relevant_docs = search_documents(question, context.index, context.documents, n_results=5)

    numbered_documents = format_documents(relevant_docs)
    question_context = f"This question is about the GitHub repository '{context.repo_name}' available at {context.github_url}. The most relevant documents are:\n\n{numbered_documents}"

    # Run the chain with the prompt variables; model name was set on LLM instantiation
    answer_with_sources = context.llm_chain.run(
        repo_name=context.repo_name,
        github_url=context.github_url,
        conversation_history=context.conversation_history,
        question=question,
        numbered_documents=numbered_documents,
        file_type_counts=context.file_type_counts,
        filenames=context.filenames
    )
    return answer_with_sources
