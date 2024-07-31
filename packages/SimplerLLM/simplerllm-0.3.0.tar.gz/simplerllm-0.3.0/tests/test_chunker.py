from SimplerLLM.language.embeddings import LLM as EmbeddingLLM, EmbeddingsProvider
from SimplerLLM.language.llm import LLM as GenerationLLM, LLMProvider
from SimplerLLM.tools.generic_loader import load_content
from SimplerLLM.tools.text_chunker import chunk_by_semantics


#from langchain_experimental.text_splitter import SemanticChunker
#from langchain_openai.embeddings import OpenAIEmbeddings



instance  = GenerationLLM.create(provider=LLMProvider.OPENAI,model_name="gpt-3.5-turbo")
embeddings_instance = EmbeddingLLM.create(provider=EmbeddingsProvider.OPENAI,model_name="text-embedding-3-small")

blog_url = "https://www.youtube.com/watch?v=3nnMJ62dJlk&pp=ygUMUkpQIHRlY2huaXFl"

content = load_content(blog_url)
#content = load_content("https://learnwithhasan.com/free-ai-chatbot-on-wordpress/")

blog = content.content

my_chunks = chunk_by_semantics(text=blog,llm_embeddings_instance=embeddings_instance,threshold_percentage=95)

#text_splitter = SemanticChunker(
#    OpenAIEmbeddings()
#)
# Process the text to create documents
#langchain_chunks = text_splitter.create_documents([blog])


print("My Chunker Results:")
print(my_chunks.num_chunks)
print(my_chunks.chunk_list)


#print("------------")
#print("Langchain Results:")
#print(len(langchain_chunks))
#print(langchain_chunks[0])