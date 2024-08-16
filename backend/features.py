from bs4 import BeautifulSoup

class WebsiteFeatures:
    def __init__(self, soup: BeautifulSoup):
        self.soup = soup

    def create_vector(self):
        return [
            self.has_title(),
            self.has_input(),
            self.has_button(),
            self.has_image(),
            self.has_submit(),
            self.has_link(),
            self.has_password(),
            self.has_email_input(),
            self.has_hidden_element(),
            self.has_audio(),
            self.has_video(),
            self.number_of_inputs(),
            self.number_of_buttons(),
            self.number_of_images(),
            self.number_of_option(),
            self.number_of_list(),
            self.number_of_TH(),
            self.number_of_TR(),
            self.number_of_href(),
            self.number_of_paragraph(),
            self.number_of_script(),
            self.length_of_title(),
            self.has_h1(),
            self.has_h2(),
            self.has_h3(),
            self.length_of_text(),
            self.number_of_clickable_button(),
            self.number_of_a(),
            self.number_of_img(),
            self.number_of_div(),
            self.number_of_figure(),
            self.has_footer(),
            self.has_form(),
            self.has_text_area(),
            self.has_iframe(),
            self.has_text_input(),
            self.number_of_meta(),
            self.has_nav(),
            self.has_object(),
            self.has_picture(),
            self.number_of_sources(),
            self.number_of_span(),
            self.number_of_table()
        ]

    def has_title(self):
        return 1 if self.soup.title and len(self.soup.title.text) > 0 else 0

    def has_input(self):
        return 1 if len(self.soup.find_all("input")) else 0

    def has_button(self):
        return 1 if len(self.soup.find_all("button")) > 0 else 0

    def has_image(self):
        return 1 if len(self.soup.find_all("image")) else 0

    def has_submit(self):
        for button in self.soup.find_all("input"):
            if button.get("type") == "submit":
                return 1
        return 0

    def has_link(self):
        return 1 if len(self.soup.find_all("link")) > 0 else 0

    def has_password(self):
        for input in self.soup.find_all("input"):
            if (input.get("type") or input.get("name") or input.get("id")) == "password":
                return 1
        return 0

    def has_email_input(self):
        for input in self.soup.find_all("input"):
            if (input.get("type") or input.get("id") or input.get("name")) == "email":
                return 1
        return 0

    def has_hidden_element(self):
        for input in self.soup.find_all("input"):
            if input.get("type") == "hidden":
                return 1
        return 0

    def has_audio(self):
        return 1 if len(self.soup.find_all("audio")) > 0 else 0

    def has_video(self):
        return 1 if len(self.soup.find_all("video")) > 0 else 0

    def number_of_inputs(self):
        return len(self.soup.find_all("input"))

    def number_of_buttons(self):
        return len(self.soup.find_all("button"))

    def number_of_images(self):
        image_tags = len(self.soup.find_all("image"))
        count = 0
        for meta in self.soup.find_all("meta"):
            if meta.get("type") or meta.get("name") == "image":
                count += 1
        return image_tags + count

    def number_of_option(self):
        return len(self.soup.find_all("option"))

    def number_of_list(self):
        return len(self.soup.find_all("li"))

    def number_of_TH(self):
        return len(self.soup.find_all("th"))

    def number_of_TR(self):
        return len(self.soup.find_all("tr"))

    def number_of_href(self):
        count = 0
        for link in self.soup.find_all("link"):
            if link.get("href"):
                count += 1
        return count

    def number_of_paragraph(self):
        return len(self.soup.find_all("p"))

    def number_of_script(self):
        return len(self.soup.find_all("script"))

    def length_of_title(self):
        return len(self.soup.title.text) if self.soup.title else 0

    def has_h1(self):
        return 1 if len(self.soup.find_all("h1")) > 0 else 0

    def has_h2(self):
        return 1 if len(self.soup.find_all("h2")) > 0 else 0

    def has_h3(self):
        return 1 if len(self.soup.find_all("h3")) > 0 else 0

    def length_of_text(self):
        return len(self.soup.get_text())

    def number_of_clickable_button(self):
        count = 0
        for button in self.soup.find_all("button"):
            if button.get("type") == "button":
                count += 1
        return count

    def number_of_a(self):
        return len(self.soup.find_all("a"))

    def number_of_img(self):
        return len(self.soup.find_all("img"))

    def number_of_div(self):
        return len(self.soup.find_all("div"))

    def number_of_figure(self):
        return len(self.soup.find_all("figure"))

    def has_footer(self):
        return 1 if len(self.soup.find_all("footer")) > 0 else 0

    def has_form(self):
        return 1 if len(self.soup.find_all("form")) > 0 else 0

    def has_text_area(self):
        return 1 if len(self.soup.find_all("textarea")) > 0 else 0

    def has_iframe(self):
        return 1 if len(self.soup.find_all("iframe")) > 0 else 0

    def has_text_input(self):
        for input in self.soup.find_all("input"):
            if input.get("type") == "text":
                return 1
        return 0

    def number_of_meta(self):
        return len(self.soup.find_all("meta"))

    def has_nav(self):
        return 1 if len(self.soup.find_all("nav")) > 0 else 0

    def has_object(self):
        return 1 if len(self.soup.find_all("object")) > 0 else 0

    def has_picture(self):
        return 1 if len(self.soup.find_all("picture")) > 0 else 0

    def number_of_sources(self):
        return len(self.soup.find_all("source"))

    def number_of_span(self):
        return len(self.soup.find_all("span"))

    def number_of_table(self):
        return len(self.soup.find_all("table"))
