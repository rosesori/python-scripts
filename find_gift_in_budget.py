"""
A script that finds products from the FakeStoreAPI that are within the inputted budget.
"""

import argparse
import json
import sys
import time

from api_client import APIClient


def parse_args(args) -> argparse.Namespace:
    """
    Parse script arguments.
    """
    parser = argparse.ArgumentParser(
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=40, width=120
        )
    )

    parser.add_argument(
        "-b", "--budget", required=True, type=int, help="User's budget to find products"
    )
    parser.add_argument(
        "-c", "--category", required=False, help="Store category to filter products on."
    )
    parser.add_argument("--id", required=False, help="Product ID to retrieve")

    args = parser.parse_args()
    return args


def create_output_file(budget_products: list[dict]) -> None:
    """
    Create a json file that contains products that were within the user's budget
    """
    filename = f"products-in-budget-{time.strftime('%Y%m%d-%H%M')}.json"
    print(f"Creating {filename} that contains products that are within the budget...")

    with open(filename, "w") as write_file:
        json.dump(budget_products, write_file, indent=4)


def filter_products_on_budget(budget: int, products):
    """
    Return products that are within the user's budget

    Args:
        budget (int): Budget that products must be equal or less than in price
        products: product list to filter
    """
    filtered_products = []

    if isinstance(products, list):
        for product in products:
            # If a product is within budget, add it to the list of filtered products
            if product["price"] <= budget:
                filtered_products.append(product)
    else:
        # If theres only one product returned
        if products["price"] <= budget:
            filter_products_on_budget.append(products)

    return filtered_products


if __name__ == "__main__":
    # Get everything after the scripts name
    args = parse_args(sys.argv[1:])
    BUDGET = args.budget

    # Create APIClient instance
    api_client = APIClient()

    if args.category and args.id:
        print(f"USAGE ERROR: You cannot use --category and --id at the same time.")
        sys.exit(1)

    # Get products from the API
    if args.category:
        unfiltered_products = api_client.get_product_by_category(
            product_category=args.category
        )
        if not unfiltered_products:
            print(f"There are no products within the {args.category} category.")
            sys.exit(0)
    elif args.id:
        unfiltered_products = api_client.get_product_by_id(product_id=args.id)
        if not unfiltered_products:
            print(f"There were no products by the ID {args.id}.")
            sys.exit(0)
    else:
        unfiltered_products = api_client.get_products()

    # Filter products on the user's budget
    products_within_budget = filter_products_on_budget(
        budget=BUDGET, products=unfiltered_products
    )
    if products_within_budget:
        create_output_file(budget_products=products_within_budget)
    else:
        print(f"There are no products in budget.")
