from translate import Translator


def translate_text():
    """Translate text from one language to another."""
    print("Welcome to the Language Translator!")
    source_lang = input("Enter the source language (e.g., 'en' for English): ").strip()
    target_lang = input("Enter the target language (e.g., 'es' for Spanish): ").strip()
    text_to_translate = input("Enter the text you want to translate: ").strip()

    if not source_lang or not target_lang or not text_to_translate:
        print("All fields are required!")
        return

    try:
        translator = Translator(from_lang=source_lang, to_lang=target_lang)
        translation = translator.translate(text_to_translate)
        print(f"\nTranslated Text ({source_lang} -> {target_lang}): {translation}")
    except Exception as e:
        print(f"Error during translation: {e}")


def main():
    """Main loop for the translator tool."""
    while True:
        translate_text()
        retry = input("\nWould you like to translate something else? (yes/no): ").strip().lower()
        if retry != "yes":
            print("Thank you for using the Language Translator! Goodbye!")
            break


if __name__ == "__main__":
    main()
