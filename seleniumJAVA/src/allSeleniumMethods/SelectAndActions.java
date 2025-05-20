package allSeleniumMethods;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.Select;

public class SelectAndActions {

	public static void main(String[] args) {
		ChromeDriver driver = new ChromeDriver();
		WebElement e=driver.findElement(By.xpath(""));
		
//		Select Class
		Select s = new Select(e);
		s.selectByIndex(0);
		s.selectByValue("");
		s.selectByVisibleText("");
		s.selectByContainsVisibleText("");
		
		s.deselectAll();
		s.deSelectByContainsVisibleText("");
		s.deselectByIndex(0);
		s.deselectByValue("");
		s.deselectByVisibleText("");
		
		s.getAllSelectedOptions();
		s.getFirstSelectedOption();
		s.getOptions();
		s.isMultiple();
		
//		Actions class
		Actions a=new Actions(driver);
		a.click();
		a.click(e);
		a.clickAndHold();
		a.clickAndHold(e);
		a.contextClick();
		a.contextClick(e);
		a.doubleClick();
		a.doubleClick(e);
		a.dragAndDrop(e, e);
		a.dragAndDropBy(e, 0, 0);
		a.getActiveKeyboard();
		a.moveToElement(e);
		a.moveToElement(e, 0, 0);
		a.moveToLocation(0, 0);
		a.moveByOffset(0, 0);
		a.sendKeys("");
		a.sendKeys(e, "");
		a.keyDown(Keys.ADD);
		a.keyUp(Keys.ADD);
		a.keyDown(e, Keys.ADD);
		a.keyUp(e, Keys.ADD);
		a.build().perform();
		a.release();
		a.release(e);
	}

}
