package wannianli;
import java.util.Scanner;//构建Scanner对象

/*
 * 万年历 
 * 2020.11.09
 * 计算闰年：
 * 年份能被四（四百）整除 || 年份除于100 !=0
 * */
public class wnl_demo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("**********万年历**********");//输出换行
		System.out.println("请输入你要查询的年份:");
		Scanner sc = new Scanner(System.in);//从键盘接受数据
		int year = sc.nextInt();//键盘输入的数据
		System.out.println("请输入你要查询的月份:");
		int month = sc.nextInt();
		boolean Rn = false;//闰年判断
		if((year%4==0 && year%100 !=0) || (year%400==0)) {
			Rn=true;
		}
		int wnDays=0;//定义
		int nf=1900;
		for(int i=nf;i<year;i++) {
			if((year%4==0 && year%100 !=0) || (year%400==0)) {
				wnDays=wnDays+366;
			}else {
				wnDays=wnDays+365;
			}
		}
		int wnMonth=0;
		int days=0;
		for(int i=1;i<=month;i++) {
			switch(i){
			case 4:
			case 6:
			case 9:
			case 11:
				days=30;
				break;
			case 2:
			if(Rn) {
				days=29;
			}else {
				days=28;
			}
			break;
			default:
				days=31;
			}
			if(i<month) {
				wnMonth=wnMonth+days;
			}
		}
		wnDays=wnDays+wnMonth+1;
		int nr=1900;
		System.out.println(year+"距"+ nr +"年，已经过去" +wnDays+"天");
		int yushu = wnDays%7;
		System.out.println("******日历展示*******");
		System.out.println("星期日\t星期一\t星期二\t星期三\t星期四\t星期五\t星期六\t");
		for(int i=1;i<=yushu;i++) {
			System.out.print("\t");
		}
		for(int i=1;i<=days;i++) {
			System.out.print(i+"\t");
			if((wnDays+i-1)%7==6)
				System.out.println();
		}
		
	}

}
