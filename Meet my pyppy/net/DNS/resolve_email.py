# legitimate use of raw DNS is for e-mails
import argparse
import dns.resolver


def resolve_hostname(hostname, indent=''):
    """"Print an A or AAAA record for `hostname`; follow CNAMEs if necessary"""
    indent += '  '

    answer = dns.resolver.query(hostname, 'A', raise_on_no_answer=False)
    if answer.rrset is not None:
        for record in answer:
            print(indent, hostname, f'has A address {record.address}')
        return

    answer = dns.resolver.query(hostname, 'AAAA', raise_on_no_answer=False)
    if answer.rrset is not None:
        for record in answer:
            print(indent, hostname, f'has AAAA address {record.address}')
        return

    answer = dns.resolver.query(hostname, 'CNAME', raise_on_no_answer=False)
    if answer.rrset is not None:
        record = answer[0]
        cname = record.address
        print(indent, hostname, f'is a CNAME alias for {cname}')
        resolve_hostname(cname, indent)
        return

    print(indent, f'ERROR: no A, AAAA or CNAME records for {hostname}')


def resolve_email_domain(domain):
    """For an email adress `name@domain` find its mail server IP adresses."""
    try:
        answer = dns.resolver.query(domain, 'MX', raise_on_no_answer=False)
    except dns.resolver.NXDOMAIN:
        print(f'Error no such domain `{domain}`')
        return

    if answer.rrset is not None:
        records = sorted(answer, key=lambda record: record.preference)
        for record in records:
            name = record.exchange.to_text(omit_final_dot=True)
            print(f'Priority {record.preference}')
            resolve_hostname(name)
    else:
        print(f'This domain has no explicit MX records')
        print(f'Attempting to resolve it as an A, AAAA or CNAME')
        resolve_hostname(domain)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find mailserver IP address')
    parser.add_argument('domain', help='domaint that you want to send an email to')
    resolve_email_domain(parser.parse_args().domain)
