package wannianli;
import java.util.Scanner;//����Scanner����

/*
 * ������ 
 * 2020.11.09
 * �������꣺
 * ����ܱ��ģ��İ٣����� || ��ݳ���100 !=0
 * */
public class wnl_demo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("**********������**********");//�������
		System.out.println("��������Ҫ��ѯ�����:");
		Scanner sc = new Scanner(System.in);//�Ӽ��̽�������
		int year = sc.nextInt();//�������������
		System.out.println("��������Ҫ��ѯ���·�:");
		int month = sc.nextInt();
		boolean Rn = false;//�����ж�
		if((year%4==0 && year%100 !=0) || (year%400==0)) {
			Rn=true;
		}
		int wnDays=0;//����
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
		System.out.println(year+"��"+ nr +"�꣬�Ѿ���ȥ" +wnDays+"��");
		int yushu = wnDays%7;
		System.out.println("******����չʾ*******");
		System.out.println("������\t����һ\t���ڶ�\t������\t������\t������\t������\t");
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
