class preprocessor:
    def __init__(self):
        self.lines = []

    def proc_body(self, body, name = "", email = ""):
        self.lines = []

        bodyLines = body.splitlines()
        for line in bodyLines:
            self.lines.append(line)

        self.lines = self.remove_EmptyLines(self.lines)

        #for line in self.lines:
            #print("-- " + line)

        print(" --------------------------------------------- ")

        header_keywords = ["subject:", "from:", "date:", "to:", "/", "forwarded"]

        donation_keywords = ["contribute", "contributes", "contributed", "donor list", "list", "fund", "donate", "donated", "donates", "match", "matched", "offer", "end-of-month", "deadline", "deadlines" "yard signs", "club", "official donor file"]
        poll_keywords_1 = ["poll", "survey", "rate", "approve"]
        poll_keywords_2 = ["o yes", "o no", "o epic", "o great", "o good", "o other", "o incredible", "o president", "o sleepy joe", "  terrible", "  poor", "  mediocre", "  other", "  yes", "  no"]
        poll_keywords = poll_keywords_1 + poll_keywords_2
        misc_keywords = ["http", "www.", ".com", ":", "product", "hat", "hats", "get it first", "get yours now", "official trump ad", "limited-edition", "@", "everything is made in the u.s.a.", "📎", "🚨"]
        body_keywords = donation_keywords + poll_keywords + misc_keywords

        footer_keywords_1 = ["thank you", "president of the united states", "headshot", "president donald j. trump", "donald j. trump", "kimberly guilfoyle", "national chair", "trump victory finance committee"]
        footer_keywords_2 = ["contributions", "trump make america great again committee", "email", "privacy policy" , "unsubscribe"]
        footer_keywords = footer_keywords_1 + footer_keywords_2

        keywords = header_keywords + body_keywords + footer_keywords

        name_start = name + " "
        name_start_comma = name + ","
        name_end = " " + name
        name_end_comma = ", " + name
        name_end_period = name + "."
        name_forms = [name_start, name_start_comma, name_end, name_end_comma, name_end_period]

        final_lines = []
        print("!!! - Checking Lines - !!!")
        for i in range(len(self.lines)):
            line_lower = self.lines[i].lower()
            isValid = True
            #print(str(i) + " : " + line_lower)
            if len(line_lower) >= 400:
                #print("LENGTH: " + str(len(line_lower)))
                isValid = False
            for name in name_forms:
                if ( name in line_lower ) :
                    #print("NAME: " + name + " -> " + line_lower)
                    isValid = False
                    break
            if ( email in line_lower ) or ( line_lower == "" ):
                if (email in line_lower):
                    #print("EMAIL: " + line_lower)
                    isValid = False
                if (line_lower == ""):
                    #print("EMPTY LINE: " + line_lower)
                    isValid = False
            for keyword in keywords:
                if (keyword in line_lower):
                    #print("KEYWORD: " + keyword + " -> " + line_lower)
                    isValid = False
            if isValid is True:
                #print("VALID: " + line_lower)
                final_lines.append(line_lower)
        print("final_lines : " + str(len(final_lines)))
        final_lines = self.remove_EmptyLines(final_lines)
        print(" <---------------------------------------------> ")
        print("END")
        #final_lines = self.final_check(final_lines)

        return final_lines

    def remove_EmptyLines(self, lines):
        emptyLines = []

        for i in range(len(lines)):
            if lines[i].isspace() == True or len(lines[i]) == 0:
                emptyLines.append(i)

        for i in reversed(emptyLines):
            del lines[i]

        return lines
