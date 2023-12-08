from duckduckgo_search import DDGS

ddgs = DDGS()

def summarizier(text2):
    query = text2
    search_results = ddgs.text(query, timelimit=1)  # Set timelimit to 0.5 seconds for less articles

    # Set the desired number of results to print
    num_results_to_print = 40
    count = 0
    info=""
    # Iterate over the search results
    for result in search_results:
        if count >= num_results_to_print:
            break
        info=info+str(result)
        count += 1
    import spacy
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(info)
    summary = " ".join([sent.text for sent in doc.sents][:2])  # Extract first two sentences as a summary
    return summary
