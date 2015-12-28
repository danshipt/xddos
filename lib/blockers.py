from __future__ import unicode_literals

from subprocess import Popen, PIPE


class GenericBlocker(object):
    def get_block_command(self, ip):
        raise Exception('Not implemented.')

    def get_unblock_command(self, ip):
        raise Exception('Not implemented.')

    def block(self, ip):
        Popen(self.get_block_command(ip), stdout=PIPE).wait()

    def unblock(self, ip):
        Popen(self.get_unblock_command(ip), stdout=PIPE).wait()


class IPTablesBlocker(GenericBlocker):
    def __init__(self):
        self.block_command = ['/sbin/iptables', '-A', 'INPUT', '-s']
        self.unblock_command = ['/sbin/iptables', '-D', 'INPUT', '-s']

    def get_block_command(self, ip):
        assert ip

        block_cmd = list(self.block_command)
        block_cmd.append(ip)
        block_cmd.append('-j')
        block_cmd.append('DROP')
        block_cmd.append('-m')
        block_cmd.append('comment')
        block_cmd.append('--comment')
        block_cmd.append("'xddos'")

        return block_cmd

    def get_unblock_command(self, ip):
        assert ip

        unblock_cmd = list(self.unblock_command)
        unblock_cmd.append(ip)
        unblock_cmd.append('-j')
        unblock_cmd.append('DROP')
        unblock_cmd.append('-m')
        unblock_cmd.append('comment')
        unblock_cmd.append('--comment')
        unblock_cmd.append("'xddos'")

        return unblock_cmd


class ApfBlocker(GenericBlocker):
    def __init__(self):
        self.block_command = ['/etc/apf/apf', '-d']  # ip comment
        self.unblock_command = ['/etc/apf/apf', '-u']  # ip comment

    def get_block_command(self, ip):
        assert ip

        block_cmd = list(self.block_command)
        block_cmd.append(ip)
        block_cmd.append('xddos')

        return block_cmd

    def get_unblock_command(self, ip):
        assert ip

        unblock_cmd = list(self.unblock_command)
        unblock_cmd.append(ip)
        unblock_cmd.append('xddos')

        return unblock_cmd
