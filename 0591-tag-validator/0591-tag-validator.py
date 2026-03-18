class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i, n = 0, len(code)

        while i < n:
            if code.startswith("<![CDATA[", i):
                # CDATA must be inside a valid tag
                if not stack:
                    return False
                j = code.find("]]>", i)
                if j == -1:
                    return False
                i = j + 3
            elif code.startswith("</", i):
                j = code.find(">", i)
                if j == -1:
                    return False
                tagname = code[i+2:j]
                if not stack or stack[-1] != tagname:
                    return False
                stack.pop()
                i = j + 1
                # once root closes, no extra content allowed
                if not stack and i < n:
                    return False
            elif code.startswith("<", i):
                j = code.find(">", i)
                if j == -1:
                    return False
                tagname = code[i+1:j]
                # ✅ strict validation: only uppercase letters, length 1–9
                if not (1 <= len(tagname) <= 9 and tagname.isalpha() and tagname.isupper()):
                    return False
                stack.append(tagname)
                i = j + 1
            else:
                # text must be inside a tag
                if not stack:
                    return False
                i += 1

        return not stack
