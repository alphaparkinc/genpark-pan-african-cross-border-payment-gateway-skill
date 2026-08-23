from client import PanAfricanCrossBorderPaymentGatewayClient

def main():
    client = PanAfricanCrossBorderPaymentGatewayClient()
    res = client.process_pan_african_payment(250.0, 'USD', 'KE', 'mobile_money')
    print('Transaction: ' + res['transaction_id'] + ' | Status: ' + res['compliance_status'])
    print('Payout: ' + str(res['payout_amount']) + ' ' + res['payout_currency'] + ' (Rate: ' + str(res['fx_rate_applied']) + ')')
    print('Rail: ' + res['settlement_rail'] + ' (' + res['settlement_speed'] + ')')

if __name__ == '__main__':
    main()
