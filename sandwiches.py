def make_sandwich(*fillings):
    print("\nMake sandwiches with ")
    for filling in fillings:
        print("-" + filling)

make_sandwich('cheese')
make_sandwich('egg','lettuce')
make_sandwich('bacon','lettuce','tomatoe')
