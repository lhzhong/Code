#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include <stdio.h>

#define threshold_diff 20 

using namespace cv;
using namespace std;

int main(int argc, char* argv[])
{
	const char* keys =
	{
		"{ f  | vidFile      | test.avi | filename of video }"
		"{ i  | imgFile      | flow | filename of flow }"
	};

	CommandLineParser cmd(argc, argv, keys);
	string vidFile = cmd.get<string>("vidFile");
	string imgFile = cmd.get<string>("imgFile");
	//string imgFile = "F:/opencv/Project/FrameDiff/tmp/";

	VideoCapture capture;
	capture.open(vidFile);
	if (!capture.isOpened()) {
		printf("Could not initialize capturing..\n");
		return -1;
	}

	int frame_num = 0;
	Mat image, prev_image, gray, prev_gray, diff_gray, frame;

	for (;;)
	{
		capture >> frame;
		if (frame.empty())
			break;
		if (frame_num == 0) {
			image.create(frame.size(), CV_8UC3);
			gray.create(frame.size(), CV_8UC1);
			prev_image.create(frame.size(), CV_8UC3);
			prev_gray.create(frame.size(), CV_8UC1);

			frame.copyTo(prev_image);
			cvtColor(prev_image, prev_gray, CV_BGR2GRAY);

			frame_num++;
			continue;
		}
		frame.copyTo(image);
		cvtColor(image, gray, CV_BGR2GRAY);
		subtract(prev_gray, gray, diff_gray);
		for (int i = 0; i<diff_gray.rows; i++)
		for (int j = 0; j<diff_gray.cols; j++)
		if (abs(diff_gray.at<unsigned char>(i, j)) >= threshold_diff)
			diff_gray.at<unsigned char>(i, j) = 255;
		else diff_gray.at<unsigned char>(i, j) = 0;

		//imshow("diff_image", diff_gray);
		//waitKey(5);

		char tmp[20];
		sprintf(tmp, "_%04d.jpg", int(frame_num));
		imwrite(imgFile + tmp, diff_gray);

		std::swap(prev_gray, gray);
		std::swap(prev_image, image);
		frame_num = frame_num + 1;

	}
	return 0;
}
