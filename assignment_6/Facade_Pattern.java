import java.util.HashMap;
import java.util.Map;

class BookInventorySystem {
    private Map<Integer, Map<String, Object>> books;

    public BookInventorySystem() {
        this.books = new HashMap<>();
    }

    public void addBook(int bookId, String title, String author) {
        Map<String, Object> bookInfo = new HashMap<>();
        bookInfo.put("title", title);
        bookInfo.put("author", author);
        bookInfo.put("available", true);
        books.put(bookId, bookInfo);
    }

    public void removeBook(int bookId) {
        books.remove(bookId);
    }

    public boolean checkAvailability(int bookId) {
        return books.containsKey(bookId) && (boolean) books.get(bookId).get("available");
    }

    public boolean borrowBook(int bookId) {
        if (checkAvailability(bookId)) {
            books.get(bookId).put("available", false);
            return true;
        } else {
            return false;
        }
    }

    public boolean returnBook(int bookId) {
        if (books.containsKey(bookId)) {
            books.get(bookId).put("available", true);
            return true;
        } else {
            return false;
        }
    }
}

class UserManagementSystem {
    private Map<Integer, String> users;

    public UserManagementSystem() {
        this.users = new HashMap<>();
    }

    public void addUser(int userId, String name) {
        users.put(userId, name);
    }

    public void removeUser(int userId) {
        users.remove(userId);
    }

    public String searchUser(int userId) {
        return users.get(userId);
    }
}

class LibraryFacade {
    private BookInventorySystem bookInventory;
    private UserManagementSystem userManagement;

    public LibraryFacade() {
        this.bookInventory = new BookInventorySystem();
        this.userManagement = new UserManagementSystem();
    }

    public void addBook(int bookId, String title, String author) {
        bookInventory.addBook(bookId, title, author);
    }

    public void removeBook(int bookId) {
        bookInventory.removeBook(bookId);
    }

    public void addUser(int userId, String name) {
        userManagement.addUser(userId, name);
    }

    public void removeUser(int userId) {
        userManagement.removeUser(userId);
    }

    public String borrowBook(int bookId, int userId) {
        if (bookInventory.borrowBook(bookId)) {
            return "Book " + bookId + " successfully borrowed by user " + userId + ".";
        } else {
            return "Book not available for borrowing.";
        }
    }

    public String returnBook(int bookId) {
        if (bookInventory.returnBook(bookId)) {
            return "Book " + bookId + " successfully returned.";
        } else {
            return "Book not found in inventory.";
        }
    }

    public boolean checkAvailability(int bookId) {
        return bookInventory.checkAvailability(bookId);
    }

    public String searchUser(int userId) {
        return userManagement.searchUser(userId);
    }
}

// Test cases
public class LibraryManagementSystemTest {
    public static void main(String[] args) {
        LibraryFacade library = new LibraryFacade();

        library.addBook(1, "Python Programming", "John Smith");
        library.addBook(2, "Java Basics", "Alice Johnson");
        library.addUser(101, "Bob");

        System.out.println(library.borrowBook(1, 101));
        System.out.println(library.borrowBook(2, 101));
        System.out.println(library.borrowBook(1, 101));

        System.out.println(library.returnBook(1));
        System.out.println(library.returnBook(3));

        System.out.println(library.checkAvailability(1));
        System.out.println(library.checkAvailability(2));

        System.out.println(library.searchUser(101));
        System.out.println(library.searchUser(102));
    }
}
