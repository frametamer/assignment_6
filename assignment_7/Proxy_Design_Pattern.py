class Document:
    def __init__(self, doc_id, title, content):
        self.doc_id = doc_id
        self.title = title
        self.content = content

class DocumentProxy:
    def __init__(self, document_storage):
        self.document_storage = document_storage

    def upload_document(self, document, user):
        if self._check_permissions(user):
            return self.document_storage.upload_document(document)
        else:
            raise PermissionError("User does not have permission to upload documents")

    def download_document(self, doc_id, user):
        if self._check_permissions(user):
            return self.document_storage.download_document(doc_id)
        else:
            raise PermissionError("User does not have permission to download documents")

    def search_documents(self, query, user):
        if self._check_permissions(user):
            return self.document_storage.search_documents(query)
        else:
            raise PermissionError("User does not have permission to search documents")

    def _check_permissions(self, user):
        return user.is_authenticated() and user.has_permission("document_management")

class DocumentStorage:
    def __init__(self):
        self.documents = {}

    def upload_document(self, document):
        self.documents[document.doc_id] = document
        return f"Document uploaded successfully: {document.title}"

    def download_document(self, doc_id):
        if doc_id in self.documents:
            return self.documents[doc_id]
        else:
            return None

    def search_documents(self, query):
        results = []
        for doc_id, document in self.documents.items():
            if query.lower() in document.title.lower() or query.lower() in document.content.lower():
                results.append(document)
        return results

class User:
    def __init__(self, username):
        self.username = username
        self.authenticated = False
        self.permissions = []

    def authenticate(self):
        self.authenticated = True

    def is_authenticated(self):
        return self.authenticated

    def grant_permission(self, permission):
        self.permissions.append(permission)

    def has_permission(self, permission):
        return permission in self.permissions

if __name__ == "__main__":
    document_storage = DocumentStorage()
    document_proxy = DocumentProxy(document_storage)

    user1 = User("user1")
    user1.authenticate()
    user1.grant_permission("document_management")

    user2 = User("user2")
    user2.authenticate()

    document1 = Document(1, "Document 1", "This is the content of Document 1")
    print(document_proxy.upload_document(document1, user1))

    try:
        print(document_proxy.upload_document(document1, user2))
    except PermissionError as e:
        print(e)

    downloaded_doc = document_proxy.download_document(1, user1)
    if downloaded_doc:
        print("Downloaded Document:", downloaded_doc.title)

    print("Search Results:", document_proxy.search_documents("Document", user1))
