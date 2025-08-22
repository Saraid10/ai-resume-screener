import nltk
try:
    print("Verifying NLTK tokenization...")
    tokens = nltk.word_tokenize("This test should now succeed.")
    print("✅ Success! NLTK found the data.")
    print("Tokens:", tokens)
except Exception as e:
    print(f"❌ Verification failed. Error: {e}")