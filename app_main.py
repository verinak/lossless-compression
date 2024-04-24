import statistics as st

message = input("Enter your message: ")

entropy = st.calculate_entropy(message)

print("Entropy:", entropy)