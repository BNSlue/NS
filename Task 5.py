import json
from datetime import datetime

class CodeSnippetManager:
    def __init__(self):
        self.snippets = {}  # Snippet storage
        self.categories = {}  # Category storage

    def add_snippet(self, name, code, category="Uncategorized"):
        snippet = {
            "name": name,
            "code": code,
            "category": category,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.snippets[name] = snippet
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(name)

    def delete_snippet(self, name):
        if name in self.snippets:
            category = self.snippets[name]["category"]
            del self.snippets[name]
            self.categories[category].remove(name)

    def retrieve_snippet(self, name):
        if name in self.snippets:
            return self.snippets[name]
        else:
            return "Snippet not found"

    def print_all_snippets(self):
        for name, snippet in self.snippets.items():
            print(f"--- {name} ---\n{snippet['code']}\n")

# Example usage
snippet_manager = CodeSnippetManager()
snippet_manager.add_snippet("hello_world", "print('Hello, World!')", "Python")
snippet_manager.add_snippet("factorial", "def factorial(n):\n    return 1 if n == 0 else n * factorial(n-1)", "Python")

# Print a specific snippet
print(snippet_manager.retrieve_snippet("hello_world"))

# Print all snippets
snippet_manager.print_all_snippets()
