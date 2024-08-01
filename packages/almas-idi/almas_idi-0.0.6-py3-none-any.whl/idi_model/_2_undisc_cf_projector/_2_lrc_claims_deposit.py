from idi_model.abstracted_packages import furtheredge_pandas as pd
from idi_model.abstracted_packages import furtheredge_numpy as np
from idi_model.data_merges.monthly_loss_ration import merge_monthly_loss_ratio


def lrc_claims_sub_module_calculation(
    output, monthly_loss_ratio_df, grouped_by_column_name="policy_no_"
):

    # cov_period_list = calculations_dict_validation.get("Coverage_period_index", None)
    # print(cov_period_list)
    # print(output.columns)
    # print(check_keys_in_df(output, cov_period_list))
    # if cov_period_list and check_keys_in_df(output, cov_period_list):
    #     output["Coverage_period_index"] = coverage_period_index(
    #         output, grouped_by_column_name
    #     )
    #     output = merge_monthly_loss_ratio_df(output)
    columns = [
        "Coverage_period_index",
        "Survival_Pc",
        "Estimated_insurance_claims_gross_of_survivals",
        "Estimated_insurance_claims_net_of_survivals",
    ]
    for col in columns:
        output[col] = 0
    output["Coverage_period_index"] = coverage_period_index(
        output, grouped_by_column_name
    )
    output = merge_monthly_loss_ratio(output, monthly_loss_ratio_df)

    output["Survival_Pc"] = survival_pc(output, grouped_by_column_name)

    output["Estimated_insurance_claims_gross_of_survivals"] = (
        estimated_insurance_claims_gross_of_survivals(output)
    )
    output["Estimated_insurance_claims_net_of_survivals"] = (
        estimated_insurance_claims_net_of_survivals(output)
    )
    return output


def calculate_coverage_period_index(group):
    counter = 0
    coverage_period_indices = []
    for status, next_status in zip(
        group["policy_status"], group["policy_status_shifted"]
    ):
        if status == "Expired":
            counter = 0
        elif status == "Coverage" and (
            next_status == "Construction"
            or next_status == "Coverage"
            or next_status == "Expired"
        ):
            counter += 1
        coverage_period_indices.append(counter)
    return coverage_period_indices


def coverage_period_index(output, grouped_by_column_name):

    output["policy_status_shifted"] = output.groupby(grouped_by_column_name)[
        "policy_status"
    ].shift(-1)

    output["Coverage_period_index"] = (
        output.groupby(grouped_by_column_name)
        .apply(calculate_coverage_period_index)
        .explode()
        .reset_index(drop=True)
    )
    return output["Coverage_period_index"]


def calculate_survival_pc(group):

    group["policy_status_shifted"] = group["policy_status"].shift(1)
    group["survival_values"] = (
        1 - group["monthly_prob_cancellation"]
    ).cumprod()

    group.loc[group["policy_status"] == "Not Started", "survival_values"] = 0
    group.loc[
        (group["policy_status"] == "Not Started")
        & (group["policy_status_shifted"] == "Construction"),
        "survival_values",
    ] = 1
    group.drop(["policy_status_shifted"], axis=1, inplace=True)

    return group["survival_values"]


def survival_pc(output, grouped_by_column_name):
    survival_series = output.groupby(grouped_by_column_name).apply(
        calculate_survival_pc
    )

    if isinstance(survival_series, pd.Series):
        survival_series = survival_series
    else:
        survival_series = survival_series.iloc[0]
    survival_series = survival_series.reset_index(level=0, drop=True)

    output["Survival_Pc"] = survival_series
    return output["Survival_Pc"]


def estimated_insurance_claims_gross_of_survivals(output):

    estimated_insurance_claims_gross_of_survivals = (
        output["total_agreed_premium"] * output["monthly_loss_ratio"]
    )

    return estimated_insurance_claims_gross_of_survivals


def estimated_insurance_claims_net_of_survivals(output):

    estimated_insurance_claims_net_of_survivals = (
        output["Estimated_insurance_claims_gross_of_survivals"]
        * output["Survival_Pc"]
    )

    return estimated_insurance_claims_net_of_survivals
