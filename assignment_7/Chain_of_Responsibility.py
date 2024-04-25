class SupportHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        pass

class HardwareSupportHandler(SupportHandler):
    def handle_request(self, request):
        if request.type == "Hardware":
            print("Hardware support team is handling request:", request)
        elif self.successor:
            self.successor.handle_request(request)

class SoftwareSupportHandler(SupportHandler):
    def handle_request(self, request):
        if request.type == "Software":
            print("Software support team is handling request:", request)
        elif self.successor:
            self.successor.handle_request(request)

class NetworkSupportHandler(SupportHandler):
    def handle_request(self, request):
        if request.type == "Network":
            print("Network support team is handling request:", request)
        elif self.successor:
            self.successor.handle_request(request)

class SupportRequest:
    def __init__(self, request_id, type, description, priority):
        self.request_id = request_id
        self.type = type
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"Request ID: {self.request_id}, Type: {self.type}, Description: {self.description}, Priority: {self.priority}"

def test_ticketing_system():
    hardware_handler = HardwareSupportHandler()
    software_handler = SoftwareSupportHandler(hardware_handler)
    network_handler = NetworkSupportHandler(software_handler)

    request1 = SupportRequest(1, "Hardware", "Monitor not working", "High")
    request2 = SupportRequest(2, "Software", "Application crashing", "Medium")
    request3 = SupportRequest(3, "Network", "Internet connection issue", "Low")
    request4 = SupportRequest(4, "Database", "Database server down", "High")

    network_handler.handle_request(request1)
    network_handler.handle_request(request2)
    network_handler.handle_request(request3)
    network_handler.handle_request(request4)

if __name__ == "__main__":
    test_ticketing_system()
