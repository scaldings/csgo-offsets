import requests

def get_offsets():
    return requests.get('https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.hpp').text


def format_offsets(offsets: str):
    temp = offsets.split('netvars {')[1].replace('} // namespace netvars', '').replace('namespace signatures {', '')
    temp = temp.replace('} // namespace signatures', '').replace('} // namespace hazedumper', '')
    return temp.replace('constexpr ::std::ptrdiff_t ', '').replace(';', '')


def save_to_file(formatted: str):
    header_file = ''
    for line in formatted.split('\n'):
        if line != '':
            header_file += '#define ' + line.replace(' =', '') + '\n'
    header = open('Offsets.h', 'w')
    header.write(header_file)
    header.close()

    python_file = ''
    for line in formatted.split('\n'):
        if line != '':
            python_file += line.split(' = ')[0] + ' = (' + line.split(' = ')[1] + ')\n'
    python = open('offsets.py', 'w')
    python.write(python_file)
    python.close()


if __name__ == '__main__':
    save_to_file(format_offsets(get_offsets()))