import pytest

pytestmark = pytest.mark.django_db


class TestLibraryModel:
    def test_return_str(self, library_factory):
        library = library_factory.create()
        assert library.__str__() == library.name


class TestBookModel:
    def test_return_str(self, book_factory):
        book = book_factory.create()
        assert book.__str__() == book.name
