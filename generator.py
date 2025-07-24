from langchain_core.runnables import RunnableLambda
from llm_connector import get_completion
from few_shot import FewShotPosts

llm = RunnableLambda(get_completion)
few_shot = FewShotPosts()


def get_length_str(length):
    return {
        "Short": "1 to 5 lines",
        "Medium": "6 to 10 lines",
        "Long": "11 to 15 lines"
    }.get(length, "6 to 10 lines")


def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)
    print("---- PROMPT ----\n", prompt)  # Optional for debugging
    response = llm.invoke(prompt)
    return response


def get_prompt(length, language, tag):
    length_str = get_length_str(length)

    prompt = (
        f"Generate a LinkedIn post using the below information. No preamble.\n\n"
        f"1) Topic: {tag}\n"
        f"2) Length: {length_str}\n"
        f"3) Language: {language}\n"
        f"If Language is Hinglish, it means a mix of Hindi and English.\n"
        f"The script should always be in English.\n"
    )

    examples = few_shot.get_filtered_posts(length, language, tag)

    if examples:
        prompt += "\n\n4) Use the writing style as per the following examples."
        for i, post in enumerate(examples[:2]):
            prompt += f"\n\nExample {i+1}:\n\n{post['text']}"
    else:
        prompt += "\n\n4) No relevant examples found. Keep the tone casual and impactful."

    return prompt


if __name__ == "__main__":
    print(generate_post("Medium", "English", "Mental Health"))