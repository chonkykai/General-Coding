def reverse_words(text):
  lst = list(text.split(" "))
  for i in range (len(lst)):
        lst[i] = lst[i][::-1]
        final = " ".join(lst)
  return final