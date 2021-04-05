{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gnbhub/gnbai20211/blob/master/week2/minseok.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "icBNDp9UlyVd"
      },
      "source": [
        "#Week2\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ELovgLOogE9x",
        "outputId": "a30edea3-e6a1-4843-94d6-9929f57f3c30"
      },
      "source": [
        "x, y = 3.14, 0\n",
        "\n",
        "print(f'x or y : {x or y}')\n",
        "print(f'x and y : {x and y}')\n",
        "print(f'not x : {not x}')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "x or y : 3.14\n",
            "x and y : 0\n",
            "not x : False\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tA1C9IzRecRO",
        "outputId": "65ccb179-8341-428d-fa04-35a04b81379e"
      },
      "source": [
        "a = [1, 2, 3  ]\n",
        "b = a #shallow copy\n",
        "\n",
        "print(f'a == b : {a == b}') #equality of value\n",
        "print(f'a is b : {a is b}') # identity of object\n",
        "\n",
        "c= list(a) #deep copy\n",
        "\n",
        "print(f'a == c: {a == c}') #equality of value\n",
        "print(f'a is c : {a is c}') # equality of object\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "a == b : True\n",
            " a is b : True\n",
            "a == c: True\n",
            "a is c : False\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DeAS9U-dgeTa",
        "outputId": "196d3290-50d3-4ee3-cd20-b9c50db9180d"
      },
      "source": [
        "fruits = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}\n",
        "print(f'fruits : {fruits}')\n",
        "\n",
        "print(f\"'orange' in fruits : {'orange' in fruits}\")\n",
        "print(f\"'grape' not in fruits : {'grape' not in fruits}\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "fruits : {'pear', 'apple', 'banana', 'orange'}\n",
            "'orange' in fruits : True\n",
            "'grape' not in fruits : True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OzXfYOgqhAr7",
        "outputId": "14e2f4b5-cf06-4e1b-d452-d7ea976bef07"
      },
      "source": [
        "a = set('abracadabra')       \n",
        "b = set('alacazam')          \n",
        "\n",
        "print(f'a | b : {a | b}')    \n",
        "print(f'a & b : {a & b}')    \n",
        "print(f'a - b : {a - b}')    \n",
        "print(f'a ^ b : {a ^ b}') # = (a - b) | (b - a)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "a | b : {'a', 'l', 'r', 'd', 'm', 'b', 'z', 'c'}\n",
            "a & b : {'c', 'a'}\n",
            "a - b : {'d', 'b', 'r'}\n",
            "a ^ b : {'d', 'r', 'm', 'b', 'l', 'z'}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uxxAjFHWfkSj",
        "outputId": "85b3d23a-ba6a-4625-be31-1b837db3bbb1"
      },
      "source": [
        "scores = {'calculus':90, 'physics':70}\n",
        "print(scores)\n",
        "\n",
        "scores = dict([('calculus',90),('physics',70)])\n",
        "print(scores)\n",
        "\n",
        "scores = dict(calculus=90, physics = 70)\n",
        "print(scores)\n",
        "\n",
        "scores['chemistry'] = 80\n",
        "print(scores)\n",
        "\n",
        "del scores['calculus']\n",
        "print(scores)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'calculus': 90, 'physics': 70}\n",
            "{'calculus': 90, 'physics': 70}\n",
            "{'calculus': 90, 'physics': 70}\n",
            "{'calculus': 90, 'physics': 70, 'chemistry': 80}\n",
            "{'physics': 70, 'chemistry': 80}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4vGwLwoGhh4I",
        "outputId": "659a7cf9-5646-4adb-d0a5-7dcb25a5504a"
      },
      "source": [
        "x = {}\n",
        "print(type(x))\n",
        "\n",
        "y = set()\n",
        "type(y)\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'dict'>\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "set"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MEwUU_6gh6B0",
        "outputId": "dec92167-3473-4f00-f810-b8939526c712"
      },
      "source": [
        "nums = [1, 4, 1, 4, 2, 1, 3, 5, 6, 2 ]\n",
        "\n",
        "squares = []\n",
        "for x in nums:\n",
        "  squares.append(x ** 2)\n",
        "\n",
        "print(squares)\n",
        "\n",
        "squares = [ x ** 2 for x in nums]\n",
        "print(squares)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1, 16, 1, 16, 4, 1, 9, 25, 36, 4]\n",
            "[1, 16, 1, 16, 4, 1, 9, 25, 36, 4]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0kyWRNAHh5-Z",
        "outputId": "158f7f22-83ad-421e-c7dd-9e4a5ba2dcff"
      },
      "source": [
        "evens = []\n",
        "for x in nums:\n",
        "  if x % 2 == 0:\n",
        "    evens.append(x)\n",
        "\n",
        "print (evens)\n",
        "\n",
        "squares = {x for x in nums if x%2 == 0}\n",
        "print(squares)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[4, 4, 2, 6, 2]\n",
            "{2, 4, 6}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kfnS90XFjv8L",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "52c039e6-4d76-4bd9-e6bc-89940d8f465c"
      },
      "source": [
        "def say_hello_world():\n",
        "  print('Hello world!')\n",
        "\n",
        "def say_hello_to(name):\n",
        "  print(f'Hello {name}!')\n",
        "\n",
        "def get_full_name(first, last):\n",
        "  '''\n",
        "  returns full name string\n",
        "  '''\n",
        "  return first+ ' '+last\n",
        "\n",
        "say_hello_world()\n",
        "say_hello_to('GNB')\n",
        "\n",
        "myname = get_full_name('YaHo', 'Mu')\n",
        "say_hello_to(myname)\n",
        "\n",
        "help(get_full_name)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Hello world!\n",
            "Hello GNB!\n",
            "Hello YaHo Mu!\n",
            "Help on function get_full_name in module __main__:\n",
            "\n",
            "get_full_name(first, last)\n",
            "    returns full name string\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Vhn6j5KZlmKi"
      },
      "source": [
        "## Object = Attribute + Method\n",
        "##        = Variable + Function\n",
        "##        = Data + Code\n",
        "구조체는 함수가 못들어감 클래스는 들어갈수 있다!\n",
        "C++에서는 구조체에도 함수 들어갈수있다고함"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_aC8WSfZpIiA",
        "outputId": "97d7b565-403d-4a18-f8c2-edcd8db05897"
      },
      "source": [
        "class Student:\n",
        "  pass   #클래스 만드는 과정, pass는 아무것도 안하는것 안에 내부적으로 __init__(self): 가 있음\n",
        "\n",
        "std_1 = Student()\n",
        "std_2 = Student()\n",
        "\n",
        "print(Student)\n",
        "print(std_1)\n",
        "print(std_2)\n",
        "\n",
        "print(isinstance(std_1, Student), isinstance(std_2, Student))\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class '__main__.Student'>\n",
            "<__main__.Student object at 0x7f26bd908c50>\n",
            "<__main__.Student object at 0x7f26bd908890>\n",
            "True True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yKlPv15IqsrY",
        "outputId": "b1b47484-054d-4f97-8b3c-10a2814ace99"
      },
      "source": [
        "class Student:\n",
        "\n",
        "  def __init__(self, first, last, gpa):\n",
        "    self.first = first\n",
        "    self.last = last\n",
        "    self.gpa = gpa\n",
        "    self.email = first + '.' + last + '@knu.ac.kr'\n",
        "\n",
        "  def fullname(self):    #self는 항상 빼먹으면 안된다!\n",
        "    return f'{self.first} {self.last}'\n",
        "\n",
        "std_1 = Student('Seunghwan', 'Do', 0.00)\n",
        "print(std_1.email)\n",
        "\n",
        "print(Student.fullname(std_1))\n",
        "print(std_1.fullname())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Seunghwan.Do@knu.ac.kr\n",
            "Seunghwan Do\n",
            "Seunghwan Do\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zAYqDtG7s_Kw",
        "outputId": "75a062b5-a907-4333-b5ef-6e9b9f9c901e"
      },
      "source": [
        "class Student:\n",
        "\n",
        "  num_of_stds = 0\n",
        "  domain = 'knu.ac.kr'\n",
        "\n",
        "  def __init__(self, first, last, gpa):\n",
        "    self.first = first\n",
        "    self.last = last\n",
        "    self.gpa = gpa\n",
        "    self.email = first + '.' + last + self.domain\n",
        "    Student.num_of_stds += 1\n",
        "\n",
        "std_1 = Student('ABC', 'Kim', 4.00) #클래스 끝나고 들여쓰기 조심할것!\n",
        "print(Student.num_of_stds)\n",
        "\n",
        "std_2 = Student('def','Lee', 3.00)\n",
        "print(Student.num_of_stds)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q_vrS5Fvvcth",
        "outputId": "f34bc3a4-bed4-4261-9dba-a99bb7b036fc"
      },
      "source": [
        "class GnBMember(Student):\n",
        "\n",
        "  domain = 'gnb.com'\n",
        "\n",
        "  def __init__(self, first, last, gpa, prog_lang):\n",
        "    super().__init__(first, last, gpa)\n",
        "    self.prog_lang = prog_lang\n",
        "\n",
        "gnb_1 = GnBMember('mem','1', 4.0, 'PYTHON')\n",
        "print(Student.num_of_stds, gnb_1.email, gnb_1.prog_lang)\n",
        "\n",
        "print(isinstance(gnb_1, GnBMember)) #gnb1은 gnbmember의 인스턴스다\n",
        "print(isinstance(gnb_1, Student))   #gnb1은 student의 인스턴스이기도하다\n",
        "\n",
        "print(issubclass(GnBMember, Student))\n",
        "\n",
        "print(issubclass(Student, Student)) ##자기자신도 서브클래스이다?"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3 mem.1gnb.com PYTHON\n",
            "True\n",
            "True\n",
            "True\n",
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
