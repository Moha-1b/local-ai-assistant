from agent import decide_action
from tools.data_cleaner import clean_csv

def main():
    print("🤖 Local AI Assistant")
    user_input = input("What do you want me to do? → ")

    decision = decide_action(user_input)

    if decision["action"] == "clean_data":
        input_file = input("Enter input CSV filename: ")
        output_file = input("Enter output CSV filename: ")

        result = clean_csv(input_file, output_file)
        print("\n✅ Result:")
        print(result)
    else:
        print("\n❌ I don't know how to do that yet.")

if __name__ == "__main__":
    main()
