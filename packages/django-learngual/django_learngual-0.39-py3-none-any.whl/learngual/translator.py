import json
import os

import gspread
from django.conf import settings
from google.oauth2.service_account import Credentials


class Translator:
    def __init__(self, sheet_id, sheet_name="Microcopy for Developer account"):
        self.sheet_id = sheet_id
        self.sheet_name = sheet_name
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = json.loads(
            getattr(settings, "LEARNGUAL_GOOGLE_BOT_GRED", None)
            or os.getenv("LEARNGUAL_GOOGLE_BOT_GRED")
            or "{}"
        )
        credentials = Credentials.from_service_account_info(creds, scopes=scopes)
        self.gc = gspread.authorize(credentials)
        self.translations = self.load_translations()

    def load_translations(self):
        sheet = self.gc.open_by_key(self.sheet_id)
        worksheet = sheet.worksheet(self.sheet_name)
        data = worksheet.get_all_values()

        self.headers = [x.upper() for x in data[0]]
        translations = {}

        for row in data[1:]:
            en_value = row[0].strip().lower()
            translations[en_value] = {
                self.headers[i]: row[i] for i in range(1, len(self.headers))
            }

        return translations

    def log_microcopy(self, text: str):
        sheet = self.gc.open_by_key(self.sheet_id)
        worksheet = sheet.worksheet(self.sheet_name)
        # Find the first empty row in the English column
        cell = worksheet.find("")
        empty_row = cell.row if cell else len(worksheet.get_all_values()) + 1
        worksheet.update_cell(empty_row, 1, text.strip().lower())
        print(f"Logged missing microcopy: {text}")

    def add_language_column(self, language: str):
        sheet = self.gc.open_by_key(self.sheet_id)
        worksheet = sheet.worksheet(self.sheet_name)
        # Add new column with target language header
        col_count = len(worksheet.row_values(1))
        worksheet.update_cell(1, col_count + 1, language.upper())
        print(f"Added new language column: {language}")
        self.load_translations()

    def translate(self, text: str, target_language: str):
        target_language = target_language.upper()
        if target_language.upper() not in self.headers:
            self.add_language_column(target_language)
            return text
        stripped_text = text.strip().lower()
        translated_dict = self.translations.get(stripped_text)
        if not translated_dict:
            if translated_dict is None:
                self.log_microcopy(text)
            return text

        translated_text = translated_dict.get(target_language, text)
        if not translated_text:
            return text

        return translated_text

    def get_translation(self, text, target_language, **kwargs):

        result = self.translate(text, target_language)
        if kwargs:
            result = self.render(result, **kwargs)

        return result

    def render(self, text: str, **kwargs):
        if not text:
            return text
        try:
            return text.format(**kwargs)
        except KeyError as e:
            raise KeyError(f"Imcomplete kwargs for {kwargs} for text {text}") from e
