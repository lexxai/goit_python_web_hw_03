# goit_python_web_hw_03
## Threads

### default run, with up-to 10 threads

```
python main.py -s picrures        
2023-08-30 06:19:21,476 [ MainThread ] Duration : 0:00:00.011639 with threads: 10
```

### default verbose run, with up-to 10 threads

```
python main.py -s picrures -v
2023-08-30 06:12:55,744 [ MainThread ] Start search
2023-08-30 06:12:55,746 [ Th-0 ] `Thread running for sort in picrures/pic1
2023-08-30 06:12:55,746 [ Th-1 ] `Thread running for sort in picrures/pic1/pip1-1
2023-08-30 06:12:55,746 [ Th-2 ] `Thread running for sort in picrures/pic2
2023-08-30 06:12:55,747 [ Th-3 ] `Thread running for sort in picrures/pic2/pic2-1
2023-08-30 06:12:55,747 [ Th-4 ] `Thread running for sort in picrures/pic2/pic2-1/pic2-1-1
2023-08-30 06:12:55,747 [ MainThread ] Wait all 5 threads
2023-08-30 06:12:55,749 [ Th-1 ] `Thread copy picrures/pic1/pip1-1/img02.tif to sort_result/tif/img02.tif
2023-08-30 06:12:55,751 [ Th-0 ] `Thread copy picrures/pic1/img02.tif to sort_result/tif/img02_c56d1186-2f70-4385-9c82-7597f37da1a8.tif
2023-08-30 06:12:55,753 [ Th-1 ] `Thread copy picrures/pic1/pip1-1/img03.tif to sort_result/tif/img03.tif
2023-08-30 06:12:55,754 [ Th-4 ] `Thread copy picrures/pic2/pic2-1/pic2-1-1/root1.tif to sort_result/tif/root1.tif
2023-08-30 06:12:55,756 [ Th-3 ] `Thread copy picrures/pic2/pic2-1/root1.tif to sort_result/tif/root1_ff472f47-d7a4-4ef8-b7d5-b439880b0c0e.tif
2023-08-30 06:12:55,754 [ Th-0 ] `Thread copy picrures/pic1/img03.tif to sort_result/tif/img03_7a0d6f1f-f432-48b3-a306-707a0e96805a.tif
2023-08-30 06:12:55,755 [ Th-1 ] `Thread copy picrures/pic1/pip1-1/img01.tif to sort_result/tif/img01.tif
2023-08-30 06:12:55,758 [ Th-3 ] `Thread copy picrures/pic2/pic2-1/root0.tif to sort_result/tif/root0.tif
2023-08-30 06:12:55,759 [ Th-4 ] `Thread copy picrures/pic2/pic2-1/pic2-1-1/root0.tif to sort_result/tif/root0.tif
2023-08-30 06:12:55,760 [ Th-0 ] `Thread copy picrures/pic1/img01.tif to sort_result/tif/img01_150e9ab3-5c27-4993-b996-155b83134f67.tif
2023-08-30 06:12:55,761 [ Th-3 ] `Thread copy picrures/pic2/pic2-1/root0.jpg to sort_result/jpg/root0.jpg
2023-08-30 06:12:55,761 [ Th-4 ] `Thread copy picrures/pic2/pic2-1/pic2-1-1/root0.jpg to sort_result/jpg/root0.jpg
2023-08-30 06:12:55,763 [ Th-3 ] `Thread copy picrures/pic2/pic2-1/root1.jpg to sort_result/jpg/root1.jpg
2023-08-30 06:12:55,764 [ Th-4 ] `Thread copy picrures/pic2/pic2-1/pic2-1-1/root1.jpg to sort_result/jpg/root1.jpg
2023-08-30 06:12:55,764 [ Th-4 ] `Thread copy picrures/pic2/pic2-1/pic2-1-1/root1.png to sort_result/png/root1.png
2023-08-30 06:12:55,764 [ Th-3 ] `Thread copy picrures/pic2/pic2-1/root1.png to sort_result/png/root1.png
2023-08-30 06:12:55,765 [ Th-3 ] `Thread copy picrures/pic2/pic2-1/root2.png to sort_result/png/root2.png
2023-08-30 06:12:55,766 [ Th-4 ] `Thread copy picrures/pic2/pic2-1/pic2-1-1/root2.png to sort_result/png/root2_1f049785-7a52-4c38-a59f-7795d87791f3.png
2023-08-30 06:12:55,767 [ MainThread ] Finish
2023-08-30 06:12:55,767 [ MainThread ] Duration : 0:00:00.022533 with threads: 10
```


### verbose run, with up-to 1 threads

```
python main.py -s picrures -t 1 -v
2023-08-30 06:18:03,031 [ MainThread ] Start search
2023-08-30 06:18:03,033 [ Th-0 ] `Thread running for sort in picrures/pic1
2023-08-30 06:18:03,035 [ MainThread ] Wait all 5 threads
2023-08-30 06:18:03,035 [ Th-0 ] `Thread copy picrures/pic1/img02.tif to sort_result/tif/img02.tif
2023-08-30 06:18:03,036 [ Th-0 ] `Thread copy picrures/pic1/img03.tif to sort_result/tif/img03.tif
2023-08-30 06:18:03,037 [ Th-0 ] `Thread copy picrures/pic1/img01.tif to sort_result/tif/img01.tif
2023-08-30 06:18:03,038 [ Th-1 ] `Thread running for sort in picrures/pic1/pip1-1
2023-08-30 06:18:03,038 [ Th-1 ] `Thread copy picrures/pic1/pip1-1/img02.tif to sort_result/tif/img02_deaf16c0-8320-4f00-9e12-2bb2dedef696.tif
2023-08-30 06:18:03,040 [ Th-1 ] `Thread copy picrures/pic1/pip1-1/img03.tif to sort_result/tif/img03_02b0cdba-f24a-4412-a257-f27434a983ee.tif
2023-08-30 06:18:03,041 [ Th-1 ] `Thread copy picrures/pic1/pip1-1/img01.tif to sort_result/tif/img01_edabb54b-7bc6-4092-8480-2df1bec64f45.tif
2023-08-30 06:18:03,042 [ Th-2 ] `Thread running for sort in picrures/pic2
2023-08-30 06:18:03,042 [ Th-3 ] `Thread running for sort in picrures/pic2/pic2-1
2023-08-30 06:18:03,043 [ Th-3 ] `Thread copy picrures/pic2/pic2-1/root1.tif to sort_result/tif/root1.tif
2023-08-30 06:18:03,044 [ Th-3 ] `Thread copy picrures/pic2/pic2-1/root0.tif to sort_result/tif/root0.tif
2023-08-30 06:18:03,045 [ Th-3 ] `Thread copy picrures/pic2/pic2-1/root0.jpg to sort_result/jpg/root0.jpg
2023-08-30 06:18:03,045 [ Th-3 ] `Thread copy picrures/pic2/pic2-1/root1.jpg to sort_result/jpg/root1.jpg
2023-08-30 06:18:03,046 [ Th-3 ] `Thread copy picrures/pic2/pic2-1/root1.png to sort_result/png/root1.png
2023-08-30 06:18:03,047 [ Th-3 ] `Thread copy picrures/pic2/pic2-1/root2.png to sort_result/png/root2.png
2023-08-30 06:18:03,047 [ Th-4 ] `Thread running for sort in picrures/pic2/pic2-1/pic2-1-1
2023-08-30 06:18:03,048 [ Th-4 ] `Thread copy picrures/pic2/pic2-1/pic2-1-1/root1.tif to sort_result/tif/root1_f86fa926-6f83-4c50-b214-6fa51cdd9eb1.tif
2023-08-30 06:18:03,050 [ Th-4 ] `Thread copy picrures/pic2/pic2-1/pic2-1-1/root0.tif to sort_result/tif/root0_01533f63-b740-416f-99a8-53aac7c5069a.tif
2023-08-30 06:18:03,051 [ Th-4 ] `Thread copy picrures/pic2/pic2-1/pic2-1-1/root0.jpg to sort_result/jpg/root0_81acdb52-33a5-4e92-af6e-efe957e7e226.jpg
2023-08-30 06:18:03,052 [ Th-4 ] `Thread copy picrures/pic2/pic2-1/pic2-1-1/root1.jpg to sort_result/jpg/root1_f8a5344b-a0df-4178-bd0e-39b10fce68a3.jpg
2023-08-30 06:18:03,053 [ Th-4 ] `Thread copy picrures/pic2/pic2-1/pic2-1-1/root1.png to sort_result/png/root1_bccf0b51-0c7a-4f55-a55f-623b8bfa994b.png
2023-08-30 06:18:03,053 [ Th-4 ] `Thread copy picrures/pic2/pic2-1/pic2-1-1/root2.png to sort_result/png/root2_efe6d272-0c2f-43e9-8cec-7e9803b6bc34.png
2023-08-30 06:18:03,054 [ MainThread ] Finish
2023-08-30 06:18:03,054 [ MainThread ] Duration : 0:00:00.022543 with threads: 1
```

# MULTICORE

##  test factorize by two methods with measure time
```
python main.py -f
Method [SYNC ONE FUNC]. Duration: 0:00:00.932339  on this system is total cpu: 4
Method [SYNC SPLIT FUNC]. Duration: 0:00:00.999651  on this system is total cpu: 4
Method [ASYNC MP POOL]. Duration: 0:00:01.191044  on this system is total cpu: 4
Threads max: 10
Method [ASYNC THREAD]. Duration: 0:00:00.886677  on this system is total cpu: 4
Method [ASYNC MP PROC PIPE]. Duration: 0:00:01.058244  on this system is total cpu: 4
Method [ASYNC MP PROC QUEUE]. Duration: 0:00:01.072359  on this system is total cpu: 4

```
