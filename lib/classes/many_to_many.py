
class Article:
    all = []


    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    def get_title(self):
        return self._title
    def set_title(self, title):
        if type(title) is not str or len(title) == 0:
            return
        self._title = title
    title = property(get_title, set_title)
        

class Author:
    def __init__(self, name):
        self._name = None
        self.name = name
        
    def get_name(self):
        return self._name
    def set_name(self, name):
        if self._name is not None:
            return
        elif type(name) is not str or len(name) == 0:
            return
        self._name = name
    name = property(get_name, set_name)
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
         new_article = Article(self, magazine, title)
         return new_article
    def topic_areas(self):
        if len(self.articles()) == 0:
             return None
        else:
          return list(set(article.magazine.category for article in self.articles()))
        

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) is str and 2 <= len(name) <= 16:
            self._name = name

    name = property(get_name, set_name)

    def get_category(self):
        return self._category

    def set_category(self, category):
        if type(category)is str and len(category) > 0:
            self._category = category

    category = property(get_category, set_category)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        

    def contributors(self):
        return list(set([article.author for article in self.articles()]))
        
    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        return list(set([article.author for article in self.articles()]))
