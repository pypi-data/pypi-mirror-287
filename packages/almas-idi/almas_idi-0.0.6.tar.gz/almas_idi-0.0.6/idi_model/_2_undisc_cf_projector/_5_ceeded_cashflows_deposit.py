from idi_model.abstracted_packages import furtheredge_numpy as np


def ceeded_cashflows_sub_module_calculation(output, run_settings):

    columns = [
        "expected_reinsurance_premium",
        "expected_reinsurance_claim_recov_cancel_refunds",
        "reinsurance_commissions_amortisation_deposit_30",
        "projected_reinsurance_commissions_deposit_30",
        "projected_reinsurance_commissions_balance",
        "projected_reinsurance_mgt_fee_deposit_30",
        "projected_reinsurance_mgt_fee_balance",
    ]
    for col in columns:
        output[col] = 0
    output["expected_reinsurance_premium"] = expected_reinsurance_premium(
        output
    )

    output["expected_reinsurance_claim_recov_cancel_refunds"] = (
        expected_reinsurance_claim_recov_cancel_refunds(output)
    )

    output["reinsurance_commissions_amortisation_deposit_30"] = (
        reinsurance_commissions_amortisation_deposit_30(
            output, run_settings["reinsurance_commissions_amortisation"]
        )
    )

    output["projected_reinsurance_commissions_deposit_30"] = (
        projected_reinsurance_comm_15pc_deposit30(
            output, run_settings["deposit_premium_rate"]
        )
    )

    output["projected_reinsurance_commissions_balance"] = (
        projected_reinsurance_comm_15pc_balance(
            output, run_settings["activation_premium_rate"]
        )
    )

    output["projected_reinsurance_mgt_fee_deposit_30"] = (
        projected_reinsurance_mgt_fee_1_45_deposit_30(
            output, run_settings["deposit_premium_rate"]
        )
    )

    output["projected_reinsurance_mgt_fee_balance"] = (
        projected_reinsurance_mgt_fee_1_45_balance(
            output, run_settings["activation_premium_rate"]
        )
    )

    return output


def expected_reinsurance_premium(output):

    expected_reinsurance_premium = (
        -output["expected_premium_income"] * output["Reinsurance_Pc"]
    )

    return expected_reinsurance_premium


# à optimiser avec amine (on peut factoriser avec reinsurance_pc)
def expected_reinsurance_claim_recov_cancel_refunds(output):

    expected_reinsurance_claim_recov_cancel_refunds = (
        output["Reinsurance_Pc"]
        * output["Estimated_insurance_claims_net_of_survivals"]
        + output["cancellation_penalties"] * output["Reinsurance_Pc"]
    )

    return expected_reinsurance_claim_recov_cancel_refunds


def reinsurance_commissions_amortisation_deposit_30(
    output, reinsurance_commissions_amortisation
):

    reinsurance_commissions_amortisation_deposit_30 = np.where(
        (output["policy_status"] == "Coverage"),
        reinsurance_commissions_amortisation / 3,
        0,
    )

    return reinsurance_commissions_amortisation_deposit_30


def projected_reinsurance_comm_15pc_deposit30(output, deposit_premium_rate):

    projected_reinsurance_comm_15pc_deposit30 = (
        deposit_premium_rate
        * output["Ceded_Comms_Rt"]
        * output["total_agreed_premium"]
        * output["Reinsurance_Pc"]
        * output["reinsurance_commissions_amortisation_deposit_30"]
    )

    return projected_reinsurance_comm_15pc_deposit30


def projected_reinsurance_comm_15pc_balance(output, activation_premium_rate):

    projected_reinsurance_comm_15pc_balance = (
        activation_premium_rate
        * output["Ceded_Comms_Rt"]
        * output["total_agreed_premium"]
        * output["Reinsurance_Pc"]
        * output["reinsurance_commissions_amortisation_deposit_30"]
    )

    return projected_reinsurance_comm_15pc_balance


def projected_reinsurance_mgt_fee_1_45_deposit_30(
    output, deposit_premium_rate
):

    projected_reinsurance_mgt_fee_1_45_deposit_30 = (
        deposit_premium_rate
        * output["Mgt_Re_Exps_Rt"]
        * output["total_agreed_premium"]
        * output["Reinsurance_Pc"]
        * output["management_expense_payment_pattern"]
    )

    return projected_reinsurance_mgt_fee_1_45_deposit_30


def projected_reinsurance_mgt_fee_1_45_balance(
    output, activation_premium_rate
):

    projected_reinsurance_mgt_fee_1_45_balance = (
        activation_premium_rate
        * output["Mgt_Re_Exps_Rt"]
        * output["total_agreed_premium"]
        * output["Reinsurance_Pc"]
        * output["claims_expense_payment_pattern"]
    )

    return projected_reinsurance_mgt_fee_1_45_balance
