class Item:
    """商品类，包含商品的基本信息"""

    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        """更新商品库存"""
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False


class ShoppingCart:
    """购物车类，管理用户选择的商品"""

    def __init__(self):
        self.items = {}  # 存储商品及其数量

    def add_item(self, item, quantity):
        """向购物车添加商品"""
        if item.id in self.items:
            self.items[item.id]['quantity'] += quantity
        else:
            self.items[item.id] = {
                'item': item,
                'quantity': quantity
            }

    def remove_item(self, item_id, quantity=None):
        """从购物车移除商品"""
        if item_id in self.items:
            if quantity is None or quantity >= self.items[item_id]['quantity']:
                del self.items[item_id]
            else:
                self.items[item_id]['quantity'] -= quantity
            return True
        return False

    def get_total(self):
        """计算购物车总价"""
        total = 0
        for item_data in self.items.values():
            total += item_data['item'].price * item_data['quantity']
        return total

    def checkout(self, payment):
        """结算购物车"""
        total = self.get_total()
        if payment < total:
            return None, "支付金额不足"

        # 更新库存
        for item_data in self.items.values():
            item = item_data['item']
            quantity = item_data['quantity']
            if not item.update_stock(quantity):
                return None, f"商品 {item.name} 库存不足"

        change = payment - total
        items_purchased = list(self.items.values())
        self.items = {}  # 清空购物车
        return change, f"支付成功！找零: {change} 元"


class ShoppingSystem:
    """购物系统类，整合商品、购物车和用户交互"""

    def __init__(self):
        self.items = {}  # 存储所有商品
        self.cart = ShoppingCart()
        self.initialize_items()

    def initialize_items(self):
        """初始化商品数据"""
        items_data = [
            (1, "苹果", 5.5, 100),
            (2, "香蕉", 3.8, 80),
            (3, "牛奶", 8.0, 50),
            (4, "面包", 6.5, 30),
            (5, "鸡蛋", 12.0, 60)
        ]

        for data in items_data:
            item = Item(*data)
            self.items[item.id] = item

    def display_items(self):
        """显示所有商品"""
        print("\n=== 商品列表 ===")
        print("ID\t名称\t价格\t库存")
        for item in self.items.values():
            print(f"{item.id}\t{item.name}\t{item.price}元\t{item.stock}个")
        print("===============\n")

    def add_to_cart(self):
        """添加商品到购物车"""
        self.display_items()
        try:
            item_id = int(input("请输入要购买的商品ID (输入0返回): "))
            if item_id == 0:
                return

            if item_id not in self.items:
                print("错误：商品ID不存在")
                return

            item = self.items[item_id]
            if item.stock <= 0:
                print(f"错误：商品 {item.name} 已售罄")
                return

            quantity = int(input(f"请输入要购买的 {item.name} 数量: "))
            if quantity <= 0:
                print("错误：数量必须大于0")
                return

            if quantity > item.stock:
                print(f"错误：库存不足，最多只能购买 {item.stock} 个")
                return

            self.cart.add_item(item, quantity)
            print(f"已添加 {quantity} 个 {item.name} 到购物车")
        except ValueError:
            print("错误：请输入有效的数字")

    def remove_from_cart(self):
        """从购物车移除商品"""
        self.display_cart()
        if not self.cart.items:
            return

        try:
            item_id = int(input("请输入要移除的商品ID (输入0返回): "))
            if item_id == 0:
                return

            if item_id not in self.cart.items:
                print("错误：购物车中没有该商品")
                return

            item_name = self.cart.items[item_id]['item'].name
            quantity = input(f"请输入要移除的 {item_name} 数量 (留空移除全部): ")

            if quantity == '':
                self.cart.remove_item(item_id)
                print(f"已从购物车移除所有 {item_name}")
            else:
                quantity = int(quantity)
                if quantity <= 0:
                    print("错误：数量必须大于0")
                    return

                self.cart.remove_item(item_id, quantity)
                print(f"已从购物车移除 {quantity} 个 {item_name}")
        except ValueError:
            print("错误：请输入有效的数字")

    def display_cart(self):
        """显示购物车内容"""
        print("\n=== 购物车 ===")
        if not self.cart.items:
            print("购物车为空")
        else:
            print("ID\t名称\t价格\t数量\t小计")
            for item_data in self.cart.items.values():
                item = item_data['item']
                quantity = item_data['quantity']
                subtotal = item.price * quantity
                print(f"{item.id}\t{item.name}\t{item.price}元\t{quantity}\t{subtotal}元")

            total = self.cart.get_total()
            print(f"----------------------")
            print(f"总计: {total} 元")
        print("===============\n")

    def process_checkout(self):
        """处理结账"""
        self.display_cart()
        if not self.cart.items:
            print("购物车为空，无法结算")
            return

        total = self.cart.get_total()
        print(f"应付金额: {total} 元")

        try:
            payment = float(input("请输入支付金额: "))
            if payment <= 0:
                print("错误：支付金额必须大于0")
                return

            change, message = self.cart.checkout(payment)
            if change is not None:
                print(message)
                print("感谢惠顾，欢迎下次再来！")
            else:
                print(message)
        except ValueError:
            print("错误：请输入有效的金额")

    def run(self):
        """运行购物系统"""
        print("\n=== 欢迎使用简易购物系统 ===")

        while True:
            print("\n请选择操作:")
            print("1. 查看商品列表")
            print("2. 添加商品到购物车")
            print("3. 从购物车移除商品")
            print("4. 查看购物车")
            print("5. 结算")
            print("0. 退出系统")

            try:
                choice = int(input("请输入选项 (0-5): "))

                if choice == 0:
                    print("感谢使用，再见！")
                    break
                elif choice == 1:
                    self.display_items()
                elif choice == 2:
                    self.add_to_cart()
                elif choice == 3:
                    self.remove_from_cart()
                elif choice == 4:
                    self.display_cart()
                elif choice == 5:
                    self.process_checkout()
                else:
                    print("错误：无效的选项，请输入0-5之间的数字")
            except ValueError:
                print("错误：请输入有效的数字")


# 程序入口
if __name__ == "__main__":
    shopping_system = ShoppingSystem()
    shopping_system.run()
