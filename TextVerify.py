import nltk
# f=open("English","r")
# # For English 
# Englishtext=f.read()
# sent_text = nltk.sent_tokenize(Englishtext) # this gives us a list of sentences
# print("English")
# print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
# i=0
# for sent in sent_text:
#     print(str(i)+" "+sent)
#     i=i+1
# f.close()
# # For French 
# f=open("French","r")
# Frenchtext=f.read()
# sent_text = nltk.sent_tokenize(Frenchtext,language='french') # this gives us a list of sentences
# print("French")
# print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
# i=0
# for sent in sent_text:
#     print(str(i)+" "+sent)
#     i=i+1
# f.close()

# For Hindi 
f=open("Hindi","r")
Frenchtext=f.read()
sent_text = nltk.sent_tokenize(Frenchtext,language='indian') # this gives us a list of sentences
print("French")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
i=0
for sent in sent_text:
    print(str(i)+" "+sent)
    i=i+1
f.close()


