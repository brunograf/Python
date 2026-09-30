from rich import print, inspect
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install


print("[bold green]Olá, Mundo![/bold green] :earth_americas:")
print("")
caixa = Panel("Esse aqui é um painel de teste :+1:", title="[bold]Título do Painel[/bold]", style="blue", border_style="red", expand=False)
print(caixa)
print("")
tabela = Table(title="Tabela de Teste", show_header=True, header_style="bold magenta")
tabela.add_column("Nome", style="dim", width=12)
tabela.add_column("Idade", justify="right")
tabela.add_row("Bruno", "26")
tabela.add_row("Juju", "35")
print(tabela)
print("")
inspect(str)
print("")
install()
print(50/0)