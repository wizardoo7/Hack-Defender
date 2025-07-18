def get_password_feedback(password):
    strong_passwords = ["P@ssw0rd!", "MyDog123!", "CyberN1nja!"]
    weak_passwords = ["12345678", "qwerty", "letmein2024", "abc123456", "pass1234"]
    if password in strong_passwords:
        return "Great! This is a strong password."
    elif password in weak_passwords:
        return "This password is too weak! Try something harder to guess."
    else:
        return "Try using symbols, numbers, and uppercase letters for strength."

def get_chatbot_response(q):
    q = q.lower()

    response_map = {
        # Passwords
        ("password", "strong password", "reuse password"): "Use strong passwords with letters, numbers & symbols. Never reuse them!",
        ("2fa", "mfa", "two-factor", "multi-factor"): "Use 2FA/MFA for stronger protection on your accounts.",
        ("password manager",): "Password managers help keep your credentials safe and secure.",

        # Phishing & Scams
        ("phishing", "fake link", "suspicious link", "fake website"): "Don’t click suspicious links or enter passwords on fake sites.",
        ("scam", "fraud", "too good to be true", "lottery"): "If it sounds too good to be true, it’s probably a scam!",
        ("otp", "one-time password"): "Never share your OTP with anyone, even if they claim to be a bank or official.",
        ("bank alert", "bvn", "nin", "atm alert"): "Scammers often use fake alerts to trick people. Always verify from your bank directly.",

        # Malware / Viruses
        ("virus", "malware", "spyware", "trojan"): "Install antivirus and don’t download from shady sites.",
        ("ransomware",): "Ransomware locks your files — back up often and avoid suspicious attachments.",
        ("antivirus", "scan", "real-time protection"): "Keep your antivirus updated and run regular scans.",
        ("update", "patch", "security fix"): "Install updates to stay protected from known vulnerabilities.",

        # Network & Wi-Fi
        ("wifi", "public network", "free internet"): "Avoid banking or shopping on public Wi-Fi without a VPN.",
        ("vpn", "virtual private network"): "VPNs protect your traffic on public Wi-Fi by encrypting your connection.",
        ("firewall",): "Firewalls block unwanted traffic and protect your network from attacks.",

        # Social Media & Privacy
        ("social media", "facebook", "instagram", "tiktok", "snapchat"): "Don’t overshare. Hackers use info to guess passwords or trick you.",
        ("privacy", "location", "tracking", "data collection"): "Check app permissions and disable unnecessary tracking.",
        ("photo", "picture", "selfie"): "Think before you share pictures — once online, it’s hard to remove.",
        ("followers", "likes", "shares"): "Likes aren’t worth your safety. Share smart and protect your info.",

        # Device Safety
        ("usb", "flash drive", "pen drive"): "Avoid using unknown USBs — they may carry viruses.",
        ("bluetooth",): "Turn off Bluetooth when not in use to prevent hacking.",
        ("camera", "microphone", "webcam"): "Cover your webcam and control mic access for privacy.",
        ("smartphone", "tablet", "android", "ios"): "Always use lock screen and keep software updated.",

        # Gaming Safety
        ("games", "gaming", "roblox", "fortnite", "pubg", "minecraft"): "Play safe! Don’t talk to strangers or download cheats.",
        ("cheat", "crack", "mod", "hacked game"): "Hacked games often contain viruses. Avoid them.",
        ("in-app purchase", "game card", "game scam"): "Never enter your card info in untrusted apps or sites.",

        # Ethics & Legal
        ("hacking", "hack", "ethical hacking"): "Hacking without permission is illegal. Ethical hackers help protect systems.",
        ("cyber law", "legal", "illegal online"): "Cyber laws protect people from online abuse, fraud, and crime.",
        ("school hack", "exam hack", "wifi hack"): "Hacking school systems is wrong. Use your skills for good.",

        # AI, Bots, and Deepfakes
        ("ai", "artificial intelligence", "chatbot", "deepfake"): "AI is powerful. Don’t trust everything you see online.",
        ("fake video", "fake audio", "voice scam"): "Verify before you believe. Scammers now use deepfake voice & video.",
        ("bot", "robot", "auto-reply"): "Bots can be helpful or harmful. Don’t give them sensitive info.",

        # Online Shopping & Payments
        ("shopping", "ecommerce", "online store"): "Shop only on secure websites with https and known brands.",
        ("card", "atm", "pin", "cvv", "credit", "debit"): "Never share your card details in chats or random websites.",
        ("paystack", "flutterwave", "opay", "kuda", "moniepoint"): "Use official apps and enable alerts for your bank transactions.",

        # Backups & Data Protection
        ("backup", "restore", "cloud"): "Back up important files to the cloud or external drive regularly.",
        ("data loss", "crash", "file recovery"): "Data can be lost. Always back up and avoid risky downloads.",

        # Kids & Parents
        ("parent", "guardian", "family", "child", "children"): "Parents should teach kids to report bad behavior and use parental controls.",
        ("bully", "cyberbully", "harassment", "online abuse"): "Block and report cyberbullies. Speak to a trusted adult.",
        ("stranger", "online stranger", "chat request"): "Never talk to strangers or meet people from the internet alone.",

        # Email & Messages
        ("email", "message", "sms", "whatsapp"): "Don’t click unknown links or download attachments in strange messages.",
        ("spam", "junk mail"): "Spam messages can be dangerous — delete them without clicking.",
        ("verification", "confirmation", "account locked"): "Be careful with messages that pressure you urgently. It could be a scam.",

        # Exams, School & Study Tools
        ("exam", "cbt", "portal", "student"): "Don’t trust random 'exam help' ads. Use your knowledge and study ethically.",
        ("google form", "quiz", "test link"): "Check who sent the link before filling forms. Some steal personal info.",

        # Thank you / Polite
        ("thank", "thanks", "good bot", "awesome"): "You're welcome! Stay safe online 💻🛡️",
        ("who are you", "your name", "what can you do"): "I'm your Cyber Mentor, here to teach you how to stay safe online!",
    }

    for keywords, response in response_map.items():
        if any(k in q for k in keywords):
            return response

    return "Great question! Always stay alert online and think before you click 🕵️‍♂️💡"
