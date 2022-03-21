# N-queen Problem
## __Nêu vấn đề:__

    N-queen là bài toán tìm cách đặt N quân hậu trên một bàn cờ có kích thước N x N sao cho không có 2 quân hậu nào có thể tấn công được nhau.

VD: với __N = 4__, ta sẽ có kết quả như sau:
<p align="center">
  <a title="4-queen" style="border: none;">
    <img src="https://media.geeksforgeeks.org/wp-content/uploads/N_Queen_Problem.jpg" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

__Input:__ Một số nguyên __N__.

__Output:__ Một ma trận nhị phân, với __1__ là vị trí của quân hậu thỏa mãn, __0__ là ô trống.

VD: Dưới đây là __output__ với __N = 4__.

$$\begin{array}{ccc}
0 & 1 & 0 & 0\\
0 & 0 & 0 & 1\\
1 & 0 & 0 & 0\\
0 & 0 & 1 & 0
\end{array}$$

## __Hướng giải quyết:__
Dễ dàng thấy được, với __N = 1__, thì vấn đề khá đơn giản, nếu __N = 2__ hoặc __N = 3__ thì sẽ không tồn tại giải pháp thích hợp cho bài toán (vô nghiệm), nên ta sẽ minh họa với __N = 4__.

### __Hướng tiếp cận không dùng Backtracking__:
    Liệt kê tất cả các trường hợp mà ta có thể đặt quân hậu trên bàn cờ và loại ra các trường hợp không thỏa mãn điều kiện.

```
While (there are untried configuration)
{
    generate the next configuration
   if queens don't attack in this configuration then
   {
      print this configuration;
   }
}
````
#### __Nhận xét__:
    Ta sẽ thấy rằng với cách này, ý tưởng sẽ khá đơn giản, tuy nhiên sẽ tốn nhiều thời gian thực thi chương trình.

### __Hướng tiếp cận với Backtracking__:

#### Ý tưởng sơ khai: ####

- Đặt mỗi quân hậu lần lượt ở những cột khác nhau, bắt đầu từ trái qua phải.
- Khi đặt quân hậu vào mỗi cột, kiểm tra xem tại đó có đụng độ với quân hậu nào khác hay không?
    
    * Nếu không, đánh dấu lại vị trí và xem nó như là một phần của __Output__.
    * Ngược lại, thực hiện quay đuôi __(Backtracking)__ và trả về __Fasle__.

#### Giải thuật: ####

    Bước 1: Bắt đầu duyệt ở hàng trên cùng của ma trận.

    Bước 2: Nếu tất cả các quân hậu tìm được vị trí thỏa mãn yêu cầu. Return True.

    Bước 3: Lần lượt duyệt tất cả các cột trên cùng một hàng.
        a) Nếu tìm được cột thỏa mãn, lưu lại vị trí và kiểm tra đệ quy xem thử liệu có dẫn đến lời giải hay không.
        b) Nếu vị trí đó dẫn đến lời giải, return True.
        c) Ngược lại, bỏ vị trí đó và (Backtrack) quay lại a).

    Bước 4: Nếu tất cả các cột trên cùng một hàng đều không thỏa thì trả về False và thực hiện Backtracking.



     



