import json
import scrapy
from datetime import datetime

class CodecademySpider(scrapy.Spider):
    name = 'codecademy'
    allowed_domains = ['codecademy.com']

    def parse(self, response):
        tmp = response.css('main > div > div > div > div:nth-child(3) > div > div > h2::text')
        hasStreaks: bool = tmp.get() == 'Streaks' if tmp else False
        username = response.css('div[data-testid="name-section"] > h1::text')
        fullname = response.css('p[data-testid="full-name-section"]::text')
        longest_streak = response.css('h3[data-testid="longest-weekly-streak"]::text')
        current_streak = response.css('h3[data-testid="current-weekly-streak"]::text')
        github = response.css('div[data-testid="site-section"] > a[data-testid="social-site-github"]')
        twitter = response.css('div[data-testid="site-section"] > a[data-testid="social-site-twitter"]')
        linkedin = response.css('div[data-testid="site-section"] > a[data-testid="social-site-linkedin"]')
        website = response.css('div[data-testid="site-section"] > a[data-testid="social-site-website"]')
        badges = response.css('main > div > div > div > div:nth-child(4) > div > div > h2::text') if hasStreaks else tmp
        last_active = response.css('div[data-testid="date-section"] > p:nth-child(1)::text')
        join_date = response.css('div[data-testid="date-section"] > p:nth-child(2)::text')
        location = response.css('div[data-testid="role-section"] > p::text')
        bio = response.css('div[data-testid="bio-section"] > p::text')

        yield {
            'username': username.getall()[1] if username else None,
            'fullname': fullname.get() if fullname else None,
            'streaks': {
                'longest': int(longest_streak.get()) if hasStreaks and longest_streak else None,
                'current': int(current_streak.get()) if hasStreaks and current_streak else None
            },
            'sites': {
                'github': github.attrib['href'] if github else None,
                'twitter': twitter.attrib['href'] if twitter else None,
                'linkedin': linkedin.attrib['href'] if linkedin else None,
                'website': website.attrib['href'] if website else None
            },
            'badges': int("".join(filter(str.isdigit, badges.get()))) if badges else None,
            'last_active': last_active.getall()[1] if last_active else None,
            'join_date': datetime.strptime(join_date.getall()[1], '%b %d, %Y').date() if join_date else None,
            'location': location.get() if location else None,
            'bio': bio.get() if bio else None
        }