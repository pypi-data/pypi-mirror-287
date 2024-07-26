import curses
from .play.fmt import Fmt
from .run.basic import ExecutionResult
from .run.unit import Unit
from .run.param import Param
from .execution import Execution
from .run.diff import Diff
from .util.ftext import Sentence, Token
from typing import List, Optional
from .play.frame import Frame
from .play.floating import Floating

from .run.wdir import Wdir
from .run.report import Report
from .settings.settings_parser import SettingsParser
import os

class CDiff:

    def __init__(self, wdir: Wdir, param: Param.Basic):
        self.param = param
        self.results: List[Token] = []
        self.wdir = wdir
        self.exit = False
        self.index = 0

        self.init = 0   # index of first line to show
        self.length = 1  # length of diff
        self.space = 0  # dy space for draw

        self.finished = False
        self.resumes: List[str] = []
        self.first_error = -1

        self.sp = SettingsParser()
        self.settings = self.sp.load_settings()
        self.first_loop = True
        self.warning: Optional[Floating] = None

    def save_settings(self):
        self.settings.geral.set_is_diff_down(self.param.is_up_down)
        self.sp.save_settings()

    def set_exit(self):
        self.exit = True

    def end_processing(self):
        return len(self.results) == len(self.wdir.unit_list)

    def get_color(self, unit: Unit):
        if unit.result == ExecutionResult.SUCCESS:
            return "G"
        if unit.result == ExecutionResult.WRONG_OUTPUT:
            return "R"
        if unit.result == ExecutionResult.EXECUTION_ERROR:
            return "Y"
        if unit.result == ExecutionResult.COMPILATION_ERROR:
            return "Y"
        return ""

    def sucesso(self):
        out1 = [
            r"  _____ __ __     __    ___  _____ _____  ___  ",
            r" / ___/|  |  |   /  ]  /  _]/ ___// ___/ /   \ ",
            r"(   \_ |  |  |  /  /  /  [_(   \_(   \_ |     |",
            r" \__  ||  |  | /  /  |    _]\__  |\__  ||  O  |",
            r" /  \ ||  :  |/   \_ |   [_ /  \ |/  \ ||     |",
            r" \    ||     |\     ||     |\    |\    ||     |",
            r"  \___| \__,_| \____||_____| \___| \___| \___/ ",
        ]

        out = out1
        _, cols = Fmt.get_size()
        for i, line in enumerate(out):
            Fmt.write(i + 4, 1, Sentence().addf("g", line).center(cols - 2, Token(" ", " ")))


    def draw_scrollbar(self):
        y_init = 3
        if not self.has_any_error():
            return   
        tr = "╮"
        br = "╯"
        vbar = "│"
        bar = []

        if self.length > self.space:
            total = self.space
            _begin = False
            _end = False
            if self.init == 0:
                _begin = True
            if self.init == self.length - self.space:
                _end = True

            # pre = int((self.init / self.length) * total)
            # pos = int((max(0, self.length - self.init - self.space) / self.length) * total)            
            # mid = total - pre - pos
            pre = int((self.init / self.length) * total)
            mid = int((self.space / self.length) * total)
            pos = (max(0, total - pre - mid))

            if _begin:
                pre -= 1
            if _end:
                pos -= 1

            if self.init > 0 and pre == 0:
                pre = 1
                pos -= 1

            if _begin:
                bar.append(tr)
            for _ in range(pre):
                bar.append(vbar)
            for _ in range(mid):
                bar.append("┃")
            for _ in range(pos):
                bar.append(vbar)
            if _end:
                bar.append(br)

        elif self.length < self.space:
            bar.append(tr)
            for i in range(self.length - 2):
                bar.append(vbar)
            bar.append(br)

        _, cols = Fmt.get_size()
        for i in range(len(bar)):
            Fmt.write(i + y_init, cols - 1, Sentence().add(bar[i]))


    def draw_top_line(self):
        # construir mais uma solução
        if len(self.results) < len(self.wdir.unit_list):
            index = len(self.results)
            unit = self.wdir.unit_list[index]
            if self.wdir.solver is None:
                return
            unit.result = Execution.run_unit(self.wdir.solver, unit)
            symbol = ExecutionResult.get_symbol(unit.result)
            color = self.get_color(unit)
            self.results.append(Token(symbol.text, color))
            if color != "G" and self.first_error == -1:
                self.first_error = len(self.results) - 1
                self.index = len(self.results) - 1


        _, cols = Fmt.get_size()
        frame = Frame(0, 0).set_size(3, cols)
        if self.wdir.solver is None:
            return
        folder = ""
        if self.wdir.source_list:
            folder = os.path.abspath(self.wdir.source_list[0])
        else:
            folder = os.path.abspath(self.wdir.solver.path_list[0])

        activity = Sentence().addf("C", folder.split(os.sep)[-2])
        solvers = Sentence()
        for i, solver in enumerate(self.wdir.solvers_names()):
            if i != 0:
                solvers.add(" ")
            solvers.addf("G/", solver)
        sources = Sentence()
        for i, source in enumerate(self.wdir.sources_names()):
            if i != 0:
                sources.add(", ")
            sources.addf("Y", source)

        delta = frame.get_dx() - solvers.len()
        left = 1
        right = 1
        if delta > 0:
            delta_left = delta // 2
            left = max(1, delta_left - activity.len())
            delta_right = delta - delta_left
            right = max(1, delta_right - sources.len())

        header = Sentence().add(activity).add("─" * left).add(solvers).add("─" * right).add(sources)

        frame.set_header(header)

        unit = self.wdir.unit_list[self.index]
        frame.write(0, 0, Sentence().add(unit.str(False)).center(frame.get_dx()))


        i = 0
        output = Sentence()
        for i, symbol in enumerate(self.results):
            foco = i == self.index
            extrap = " " if not foco else ">"
            extras = " " if not foco else "<"
            output.add(extrap).addf(symbol.fmt, str(i).zfill(2)).add(symbol).add(extras)

        if self.index * 5 > frame.get_dx():
            output.cut_begin((self.index + 1) * 5 - frame.get_dx())

        frame.set_footer(output, "")
        frame.draw()
        
    def draw_guide_line(self):
        cmds = (Sentence()
        .add(" ")
        .addf("/G", "Sair[q]")
        .add(" ")
        .addf("/Y", "Navegar[wasd]")
        .add(" ")
        .addf("/C", "Executar[e]")
        .add(" ")
        .addf("/M", "MudarVisão[m]")
        .add(" ")
        )
        lines, cols = Fmt.get_size()
        Fmt.write(lines - 1, 0, cmds.center(cols, Token(" ")))

    def has_any_error(self):
        results = [unit.result for unit in self.wdir.unit_list]
        if ExecutionResult.EXECUTION_ERROR not in results and ExecutionResult.WRONG_OUTPUT not in results and ExecutionResult.COMPILATION_ERROR not in results:
            return False
        return True          

    def draw_diff(self, unit: Unit):
        lines, cols = Fmt.get_size()
        self.space = lines - 4
        frame = Frame(2, -1).set_inner(self.space, cols - 1).set_border_square()

        if not self.has_any_error():
            self.sucesso()
            return        
        Report.set_terminal_size(cols)
        if self.param.is_up_down:
            line_list = Diff.mount_up_down_diff(unit, curses=True)
        else:
            line_list = Diff.mount_side_by_side_diff(unit, curses=True)

        self.length = max(1, len(line_list))

        if self.length - self.init < self.space:
            self.init = max(0, self.length - self.space)

        if self.init >= self.length:
            self.init = self.length - 1

        if self.init < self.length:
            line_list = line_list[self.init:]
        for i, line in enumerate(line_list):
            frame.write(i, 0, Sentence().add(line))
        return

    def load_autoload_warning(self):
        if not self.wdir.is_autoload():
            return
        warning = Floating().set_header(" Atenção ").warning()
        warning.put_text("")
        warning.put_sentence(Sentence().addf("r", "Todos") + " os arquivos de código da pasta foram carregados automaticamente")
        solver = self.wdir.solver
        solvers = [] if solver is None else solver.path_list
        warning.put_text("")
        loaded = Sentence().add("Códigos: ")
        for i, file in enumerate(solvers):
            if i != 0:
                loaded.add(", ")
            loaded.addf("g", os.path.basename(file))
        warning.put_sentence(loaded)
        sources = self.wdir.source_list
        loaded = Sentence().add("Testes: ")
        for i, file in enumerate(sources):
            if i != 0:
                loaded.add(", ")
            loaded.addf("y", os.path.basename(file))

        warning.put_sentence(loaded)
        warning.put_text("")
        warning.put_text("Você também pode escolher quais arquivos deseja executar")
        warning.put_text("chamando o comando 'tko run' com os códigos desejados")
        warning.put_text("")
        warning.put_sentence(Sentence().addf("c", "tko run <arquivos> cases.tio")) 
        warning.put_text("")
        warning.put_sentence(Sentence().addf("r", "Exemplo: ").addf("c", "tko run main.c lib.c cases.tio")) 
        warning.put_text("")

        self.warning = warning

    def main(self, scr):
        curses.curs_set(0)  # Esconde o cursor
        Fmt.init_colors()  # Inicializa as cores
        Fmt.set_scr(scr)  # Define o scr como global
        while not self.exit:
            if self.first_loop:
                self.first_loop = False
                self.load_autoload_warning()
            Fmt.erase()
            self.draw_top_line()
            unit = self.wdir.unit_list[self.index]
            self.draw_diff(unit)
            self.draw_scrollbar()
            self.draw_guide_line()

            if self.warning is not None and self.warning.is_enable():
                self.warning.draw()
            if not self.end_processing():
                Fmt.refresh()
                continue

            if self.warning is not None and self.warning.is_enable():
                input = self.warning.get_input()
            else:
                input = Fmt.getch()

            if input == ord('q'):
                self.set_exit()
            elif input == curses.KEY_LEFT or input == ord('a'):
                self.index = max(0, self.index - 1)
                self.init = 0
            elif input == curses.KEY_RIGHT or input == ord('d'):
                self.index = min(len(self.results) - 1, self.index + 1)
                self.init = 0
            elif input == curses.KEY_DOWN or input == ord('s'):
                self.init += 1
            elif input == curses.KEY_UP or input == ord('w'):
                self.init = max(0, self.init - 1)
            elif input == ord('m'):
                self.param.is_up_down = not self.param.is_up_down
                self.save_settings()
                self.init = 0
            elif input == ord('e'):
                if self.wdir.solver is not None:
                    if self.wdir.is_autoload():
                        self.wdir.autoload()
                    self.wdir.solver.prepare_exec()
                self.results = []
                self.first_error = -1
                

    def run(self):
        curses.wrapper(self.main)
