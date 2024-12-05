from yandex_cloud_ml_sdk import YCloudML
from app.config import Config, load_config

config: Config = load_config()

sdk = YCloudML(folder_id=config.gpt.folder_id, auth=config.gpt.auth)


model = sdk.models.completions("yandexgpt")
model = model.configure(temperature=0.1)


async def get_summarization(video_text):
    try:
        prompt = (
            "Summarize the main points and their comprehensive explanations from below text, "
            "presenting them under appropriate headings. Use various Emoji to symbolize different sections, "
            "and format the content as a cohesive paragraph under each heading. Ensure the summary is clear, "
            "detailed, and informative, reflecting the executive summary style found in news articles. "
            "Avoid using phrases that directly reference 'the script provides' to maintain a direct and objective tone.\n\n"
            "### VIDEO TEXT SCOPE ###\n"
            f"{video_text}"
        )

        summarization = model.run(prompt)
        result = ""
        for alternative in summarization:
            result += alternative.text

        return result

    except Exception as e:
        print(f"An error occurred during summarization: {str(e)}")
        return None
