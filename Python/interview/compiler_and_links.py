"""
Объясните процесс работы компилятора и ссылок в Python
Компиляция и использование ссылок (связывание) позволяет новым расширениям
корректно компилироваться без каких-либо ошибок, а процесс связывания может
быть совершен только тогда, когда процедура компиляции проходит успешно.
При использовании динамической загрузки, она определяется стилем операционной
системы. Python интерпретатор может быть использован для обеспечения
динамической загрузки установочных файлов конфигурации.  В дальнейшем
это действие приведет в пересборке интерпретатора.

Для этого необходимо предпринять следующие шаги:
Создать файл с любым именем на любом языке, который поддерживается
компилятором вашей операционной системы. Например, c;
Поместить этот файл в директорию «Modules» используемого дистрибутива;
Добавить строку в файл Setup.local, который располагается в директории «Modules»;
Запустите файл, используя spam comp.o;
После удачного запуска необходимо перестроить интерпретатор с помощью
команды make в каталоге верхнего уровня;
При изменении файла запустите rebuildMakefile с помощью подобной команды  ‘make Makefile’.
"""