class Conference:

    def __init__(self, log_file_name):
        self.log_file_name = log_file_name

    def add_attendee(self, attendee):
        with open(self.log_file_name, "a") as log_file:
            name = attendee.name
            company = attendee.company
            state = attendee.state
            email = attendee.email
            log_file.write("{n} || {e} || {c} || {s}\n".format(n=name, e=email, c=company, s=state))

    def delete_attendee(self, name):
        with open(self.log_file_name, "r") as log_file_in:
            data = log_file_in.readlines()
            with open(self.log_file_name, "w") as log_file_out:
                for line in data:
                    if name not in line:
                        log_file_out.write(line)

    def display_attendee(self, name):
        with open(self.log_file_name, "r") as log_file:
            for line in log_file:
                l = line.split("||")
                if name in l[0]:
                    print(line)

    def attendee_location(self, state):
        with open(self.log_file_name, "r") as log_file:
            data = log_file.readlines()
            for line in data:
                if state in line:
                    l = line.split("||")
                    print(l[0], l[1])

    def attendee_contact(self):
        with open(self.log_file_name, "r") as log_file:
            data = log_file.readlines()
            for line in data:
                l = line.split("||")
                print(l[0], l[1])



