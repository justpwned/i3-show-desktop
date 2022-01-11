from i3ipc import Connection
import argparse


i3_command_orig = Connection.command
def i3_command_debug(self, command):
    result = i3_command_orig(self, command)[0]
    result_message = "OK" if result.success else result.error
    print(f'{command}: {result_message}')


def show_ws(i3, ws):
    for w in ws:
        i3.command(f'workspace {w}')


def get_saved_ws_from_file(filename):
    return open(filename).readline().split()


def save_ws_to_file(filename, ws):
    with open(filename, 'w') as f:
        f.write(' '.join(ws))


def parse_args():
    parser = argparse.ArgumentParser(description="""Show desktop/Minimize all windows like functionality
            present on any major DE of any OS.""")
    parser.add_argument('-c', '--config', action='store_true', help='generate config file additions, \
            specify --start argument to change frist unused workspace')
    parser.add_argument('-s', '--start', type=int, default=11, help='first free workspace')
    parser.add_argument('-d', '--debug', action='store_true', help='print debug messages')
    return parser.parse_args()


def generate_config(i3, start):
    ws_binds = []
    outputs = (o.name for o in i3.get_outputs() if 'root' not in o.name)
    for o in outputs:
        ws_binds.append(f'workspace {start} output {o}')
        start += 1
    return '\n'.join(ws_binds)


def main():
    i3 = Connection()
    args = parse_args()
    if args.config:
        config = generate_config(i3, args.start)
        print(config)
        return

    start_ws = args.start
    if args.debug:
        Connection.command = i3_command_debug
    start_ws = args.start

    logfile = '/tmp/i3-show-desktop.log'
    outputs = len(i3.get_outputs()) - 1
    redundant_ws = {str(ws) for ws in range(start_ws, start_ws + outputs)}
    visible_ws = {w.name for w in i3.get_workspaces() if w.visible}

    if visible_ws == redundant_ws:
        ws = get_saved_ws_from_file(logfile)
        show_ws(i3, ws)
    else:
        save_ws_to_file(logfile, visible_ws)
        show_ws(i3, redundant_ws)


if __name__ == '__main__':
    main()
