def getSearchResults(words, queries):
    # make a list that appends whichever words that queries matches with words
    # return that list
    main = []
    for i in queries:
        anagram = []
        sorted_queries = sorted(list(i))
        for x in words:
            sorted_words = sorted(list(x))
            if len(list(i)) == len(list(x)):
                count = 0
                for j in range(len(sorted_queries)):
                    if sorted_queries[j] == sorted_words[j]:
                        count += 1
                if count == len(sorted_words):
                    anagram.append(x)
                    
        main.append(sorted(anagram))

        # res = set(test_list).issubset(target_list)
    return main

                



print(getSearchResults(["allot", "cat", "peach", "dusty", "act", "cheap"], ["tac", "study", "peahc"]))
# print(getSearchResults(["emits", "items", "baker", "times", "break"],["mites", "brake"] ))