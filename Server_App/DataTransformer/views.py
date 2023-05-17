from django.shortcuts import render

def process_video(request):
    if request.method == 'POST':
        # Xử lý video đã ghi lại
        print('haha')
        # Trả về template hoặc thông báo thành công
        return render(request, 'process_video.html')

    # Trả về template mặc định nếu không phải yêu cầu POST
    return render(request, 'default_template.html')