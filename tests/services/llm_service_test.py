from app.services.llm_service import LLMService

def test():
    print("test is starting ...\n")

    llm = LLMService()
    message = "AI is"
    print(llm.generate(message=message))

    print("\ntest has finished ...")

if __name__ == "__main__":
    test()
