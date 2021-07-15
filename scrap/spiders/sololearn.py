import scrapy

class SololearnSpider(scrapy.Spider):
    name = 'sololearn'
    allowed_domains = ['sololearn.com']

    def parse(self, response):
        username = response.css('p.sl-p-details__name--text::text')
        xp = response.css('#main > div > div > div > div > div > div.sl-p-container__center > div.sl-p-details.light > div.sl-p-details__info > div:nth-child(2) > button:nth-child(2) > span::text')
        followers = response.css('#main > div > div > div > div > div > div.sl-p-container__center > div.sl-p-details.light > div.sl-p-details__info > div:nth-child(2) > button:nth-child(2) > span::text')

        yield {
            'username': username.getall() if username else None,
            'xp': xp.getall() if xp else None,
            'followers': followers.getall() if followers else None,
            # 'fullname': fullname.get() if fullname else None,
            # 'streaks': {
            #     'longest': int(longest_streak.get()) if hasStreaks and longest_streak else None,
            #     'current': int(current_streak.get()) if hasStreaks and current_streak else None
            # },
            # 'sites': {
            #     'github': github.attrib['href'] if github else None,
            #     'twitter': twitter.attrib['href'] if twitter else None,
            #     'linkedin': linkedin.attrib['href'] if linkedin else None,
            #     'website': website.attrib['href'] if website else None
            # },
            # 'badges': int("".join(filter(str.isdigit, badges.get()))) if badges else None,
            # 'last_active': last_active.getall()[1] if last_active else None,
            # 'join_date': datetime.strptime(join_date.getall()[1], '%b %d, %Y').date() if join_date else None,
            # 'location': location.get() if location else None,
            # 'bio': bio.get() if bio else None
        }