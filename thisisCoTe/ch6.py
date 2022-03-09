class Ch6:
    @staticmethod
    def main():
        pass

    @staticmethod
    def replace_elem():
        n, k = map(int, input('두개의 숫자를 입력해주세요 구분자는 ,').split(','))
        list_a = [1, 2, 5, 4, 3]
        list_b = [5, 5, 6, 6, 5]
        list_a.sort()
        list_b.sort(reverse=True)

        for i in range(3):
            if list_a[i] >= list_b[i]:
                break
            else:
                list_a[i], list_b[i] = list_b[i], list_a[i]

        print(sum(list_a))
