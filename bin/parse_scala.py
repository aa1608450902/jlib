import logging


class ParseScala:
    def parse(self, file_path):
        logging.info("scala file: {}".format(file_path))
        fp = open(file_path, 'r')
        content = fp.read()
        # content = '''"casdjkcbnasljd\\"'''
        # content += " "
        # logging.info(fp.read())
        fp1 = open("./test/tt1.scala", "w+")
        fp0 = open("./test/tt0.scala", "w+")
        fp2 = open("./test/tt2.scala", "w+")
        res = self.loop(content)
        res = self.remove_empty_line(res)
        fp1.write(res)
        res = self.loop_func(res)
        fp2.write(res)
        fp0.write(content)
        fp0.close()
        fp1.close()
        fp2.close()


    @staticmethod
    def loop(ctx):
        _r = ""

        former_type = 0
        # hold_space = ""
        hold_string = ""
        is_escape_open = False
        # brace_count = 0

        index = 0
        context_length = len(ctx)
        while index < context_length:
            let = True
            if former_type == 0:
                if ctx[index] == '/' and index + 1 < context_length and ctx[index + 1] == '*':
                    former_type = 1
                    index += 1
                    let = False
                elif ctx[index] == '/' and index + 1 < context_length and ctx[index + 1] == '/':
                    former_type = 3
                    index += 1
                    let = False
                elif ctx[index] == '"':
                    former_type = 2
                    let = False
                elif ctx[index] == '\'':
                    if index + 2 < context_length and ctx[index + 2] == '\'':
                        _r += "'{}'".format(ctx[index + 1])
                        index += 2
                        let = False
                    else:
                        logging.error("single char error")
                pass
            elif former_type == 1:
                if ctx[index] == '*' and index + 1 < context_length and ctx[index + 1] == '/':
                    former_type = 0
                    index += 1
                let = False
            elif former_type == 2:
                if is_escape_open:
                    hold_string += ctx[index]
                    is_escape_open = False
                else:
                    if ctx[index] == '"' and not is_escape_open:
                        _r += '"' + hold_string + '"'
                        hold_string = ""
                        former_type = 0
                    elif ctx[index] == '\\' and not is_escape_open:
                        hold_string += ctx[index]
                        is_escape_open = True
                    else:
                        hold_string += ctx[index]
                let = False
            elif former_type == 3:
                if ctx[index] == '\n':
                    former_type = 0
                else:
                    let = False
            else:
                pass
            if let:
                _r += ctx[index]
            index += 1
        logging.info("hold_string: {}".format(hold_string))
        logging.info(_r)
        return _r

    @staticmethod
    def loop_func(ctx):
        _r = ""
        index = 0
        context_length = len(ctx)
        is_brace_open = False
        brace_count = 0
        while index < context_length:
            let = True
            if not is_brace_open:
                if ctx[index] == '{':
                    brace_count += 1
                    is_brace_open = True
                    # let = False
            else:
                if brace_count == 1:
                    pass
                else:
                    let = False

                if ctx[index] == '{':
                    brace_count += 1
                    if brace_count == 2:
                        _r += "{}"
                    let = False
                elif ctx[index] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        is_brace_open = False
                    else:
                        let = False
            if let:
                _r += ctx[index]
            index += 1
        return _r

    @staticmethod
    def remove_empty_line(ctx):
        lines = ctx.split('\n')
        # r_lines = []
        _r = ""
        for line in lines:
            if not ParseScala.is_empty_line(line):# and "import" not in line and "package" not in line:
                _r += line + "\n"
                # r_lines.append(line)
        return _r

    @staticmethod
    def is_empty_line(seq):
        s = ""
        for c in seq:
            if c in [' ', '\t']:
                continue
            else:
                s += c
        if len(s) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)
    logging.info("parse-java-project")
    # p = Parser("/home/aiyo/lea/gradle-5.6/src")
    # p.parse()
    p = ParseScala()
    p.parse("/home/aiyo/workspace/spark-src/org/apache/spark/rdd/RDD.scala")