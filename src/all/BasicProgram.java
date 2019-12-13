package all;

import org.openqa.selenium.chrome.ChromeDriver;

public class BasicProgram {
	public static void main(String[] args) {
		System.setProperty("webdriver.chrome.driver","D:\\SW\\chromedriver.exe");
		ChromeDriver d = new ChromeDriver();
		d.get("https://www.google.co.in/");
		d.manage().deleteAllCookies();
		d.close();
		d.quit();
	}
}
