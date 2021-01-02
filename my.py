# coding=utf-8
import time

from controller import Controller
from setting import Setting
from wait_opration import WaitOperation


def run():
	setting = Setting()

	user = setting.user
	password = setting.password
	tick = setting.tick
	timeout = setting.timeout
	loading = setting.loading

	# 启动浏览器
	controller = Controller()
	driver = controller.driver

	# 启动各种功能
	wait_operation = WaitOperation(driver)

	# 登录
	controller.login(user, password)
	# anticaptcha = Anticaptcha()
	# captcha_ans = anticaptcha.run()
	print('输入验证码并点击登录后，点击确定关闭浏览器提示的修改密码')

	# 等待标题出现
	wait_operation.by_class("headerNav", 5)
	time.sleep(loading)

	# 关闭改密码
	try:
		driver.find_element_by_xpath("/html/body/div[13]/div[1]/div/div/a[1]").click()
	except Exception as e:
		print(e)
		time.sleep(loading)
		driver.find_element_by_xpath("/html/body/div[13]/div[1]/div/div/a[1]").click()
	print("Password window closed.")

	# 点到表单所在位置
	driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/h2").click()
	time.sleep(tick)
	driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[4]/ul/li[1]/div/a').click()
	time.sleep(loading)  # 数据加载中

	# 选择主体业态
	# TODO 还有bug
	print("请选择主体业态，选择完成后输入在命令行输入y并按回车。")
	while True:
		inp = input()
		if inp == 'y' or inp == 'Y':
			break

	select_list = driver.find_element_by_id('txtBodyIndustry')
	js = 'arguments[0].click()'
	driver.execute_script(js, select_list)
	time.sleep(3)

	all_options = select_list.find_elements_by_tag_name("option")
	for option in all_options:
		print("选项显示的文本：", option.text)
		print("选项值为：", option.get_attribute("value"))
		if option.get_attribute("value") == '3':
			print(option)
			driver.execute_script(js, option)
			time.sleep(tick)
	time.sleep(loading)

	# 选择监督状态
	driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div[3]/div/span/div[1]/table/tbody/tr[3]/td[4]/input[2]').click()
	time.sleep(tick)
	# 点击查询按钮
	driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div[3]/div/span/div[1]/table/tbody/tr[4]/td[5]/div/div/button').click()
	# 数据加载中
	time.sleep(loading)

	"""循环操作表单"""
	for store_idx in range(1, 51):
		# 点开表单
		driver.find_element_by_xpath('//*[@id="tb"]/tr[{}]/td[9]/a'.format(store_idx)).click()
		# 数据加载中
		time.sleep(loading)

		# 获取类别（食品制售）
		food_type = driver.find_element_by_xpath('//*[@id="outDiv"]/table/tbody/tr[3]/td[2]').text

		# 点击新增日常监督检查
		driver.find_element_by_xpath('//*[@id="RCJD"]/a/span').click()
		# 加载中
		time.sleep(loading)

		# 点击(请选择)
		driver.find_element_by_xpath('//*[@id="AddUserUl"]/ul/li[1]/a[2]/span').click()

		# 点击选择同事，点击提交
		time.sleep(tick * 4)
		name_list = driver.find_elements_by_name('userName')
		for name in name_list:
			name_check = name.get_attribute("value")
			if name_check == '张立明':
				name.click()
		time.sleep(tick)
		driver.find_element_by_xpath('/html/body/div[14]/div[2]/div/div[2]/ul/li[1]/div/div/button').click()

		# 点击生成静态风险
		# 判断是否已经选择了食品类型
		try:
			content = '(未生成静态风险评分)'
			if content == driver.find_element_by_xpath('//*[@id="yesNo"]').text:
				print('请选择静态风险并生成，保存完毕后在此窗口内输入 y 并按回车。')
				while True:
					cmd = input()
					if cmd == 'y' or cmd == 'Y':
						break
		except Exception as e:
			print(e)
			print('已经选择过了静态风险，继续。')
		
		# 不申请回避
		driver.find_element_by_xpath('//*[@id="SSHB"]/label[3]/input').click()

		# 点击提交按钮
		driver.find_element_by_xpath('//*[@id="btnGiveUp"]/div/div/button').click()
		time.sleep(tick * 2)  # TODO sleep tick * 2

		# 点击保存
		driver.find_element_by_xpath('//*[@id="btnSave"]/div/div/button').click()
		time.sleep(loading)  # TODO 改成wait_opration识别？？？

		# 点回日常监督
		driver.find_element_by_xpath('//*[@id="navTab"]/div[1]/div/ul/li[3]/a[1]/span').click()
		time.sleep(tick)

	# 运行结束
	print("如果你看到了这里，表明运行已结束。")
	time.sleep(60)


if __name__ == '__main__':
	run()
