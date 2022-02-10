
# constructor

`Type Of Function: nonpayable`

## Inputs

* _owner `(Type Of Input: address)`
* _dualRewardsDistribution `(Type Of Input: address)`
* _rewardsTokenA `(Type Of Input: address)`
* _rewardsTokenB `(Type Of Input: address)`
* _stakingToken `(Type Of Input: address)`

# OwnerChanged

`Type: event` 

## Inputs

* oldOwner `(Type Of Input: address)`
* newOwner `(Type Of Input: address)`

# OwnerNominated

`Type: event` 

## Inputs

* newOwner `(Type Of Input: address)`

# PauseChanged

`Type: event` 

## Inputs

* isPaused `(Type Of Input: bool)`

# Recovered

`Type: event` 

## Inputs

* token `(Type Of Input: address)`
* amount `(Type Of Input: uint256)`

# RewardAdded

`Type: event` 

## Inputs

* rewardA `(Type Of Input: uint256)`
* rewardB `(Type Of Input: uint256)`
* periodFinish `(Type Of Input: uint256)`

# RewardPaid

`Type: event` 

## Inputs

* user `(Type Of Input: address)`
* rewardToken `(Type Of Input: address)`
* reward `(Type Of Input: uint256)`

# Staked

`Type: event` 

## Inputs

* user `(Type Of Input: address)`
* amount `(Type Of Input: uint256)`

# Withdrawn

`Type: event` 

## Inputs

* user `(Type Of Input: address)`
* amount `(Type Of Input: uint256)`

# acceptOwnership

`Type: function` `Type Of Function: nonpayable`

## Inputs


# balanceOf

`Type: function` `Type Of Function: view`

## Inputs

* account `(Type Of Input: address)`

# dualRewardsDistribution

`Type: function` `Type Of Function: view`

## Inputs


# earnedA

`Type: function` `Type Of Function: view`

## Inputs

* account `(Type Of Input: address)`

# earnedB

`Type: function` `Type Of Function: view`

## Inputs

* account `(Type Of Input: address)`

# exit

`Type: function` `Type Of Function: nonpayable`

## Inputs


# getReward

`Type: function` `Type Of Function: nonpayable`

## Inputs


# lastPauseTime

`Type: function` `Type Of Function: view`

## Inputs


# lastTimeRewardApplicable

`Type: function` `Type Of Function: view`

## Inputs


# lastUpdateTime

`Type: function` `Type Of Function: view`

## Inputs


# nominateNewOwner

`Type: function` `Type Of Function: nonpayable`

## Inputs

* _owner `(Type Of Input: address)`

# nominatedOwner

`Type: function` `Type Of Function: view`

## Inputs


# notifyRewardAmount

`Type: function` `Type Of Function: nonpayable`

## Inputs

* rewardA `(Type Of Input: uint256)`
* rewardB `(Type Of Input: uint256)`
* rewardsDuration `(Type Of Input: uint256)`

# owner

`Type: function` `Type Of Function: view`

## Inputs


# paused

`Type: function` `Type Of Function: view`

## Inputs


# periodFinish

`Type: function` `Type Of Function: view`

## Inputs


# recoverERC20

`Type: function` `Type Of Function: nonpayable`

## Inputs

* tokenAddress `(Type Of Input: address)`
* tokenAmount `(Type Of Input: uint256)`

# rewardPerTokenA

`Type: function` `Type Of Function: view`

## Inputs


# rewardPerTokenAStored

`Type: function` `Type Of Function: view`

## Inputs


# rewardPerTokenB

`Type: function` `Type Of Function: view`

## Inputs


# rewardPerTokenBStored

`Type: function` `Type Of Function: view`

## Inputs


# rewardRateA

`Type: function` `Type Of Function: view`

## Inputs


# rewardRateB

`Type: function` `Type Of Function: view`

## Inputs


# rewardsA

`Type: function` `Type Of Function: view`

## Inputs

*  `(Type Of Input: address)`

# rewardsB

`Type: function` `Type Of Function: view`

## Inputs

*  `(Type Of Input: address)`

# rewardsTokenA

`Type: function` `Type Of Function: view`

## Inputs


# rewardsTokenB

`Type: function` `Type Of Function: view`

## Inputs


# setPaused

`Type: function` `Type Of Function: nonpayable`

## Inputs

* _paused `(Type Of Input: bool)`

# stake

`Type: function` `Type Of Function: nonpayable`

## Inputs

* amount `(Type Of Input: uint256)`

# stakingToken

`Type: function` `Type Of Function: view`

## Inputs


# totalSupply

`Type: function` `Type Of Function: view`

## Inputs


# userRewardPerTokenAPaid

`Type: function` `Type Of Function: view`

## Inputs

*  `(Type Of Input: address)`

# userRewardPerTokenBPaid

`Type: function` `Type Of Function: view`

## Inputs

*  `(Type Of Input: address)`

# withdraw

`Type: function` `Type Of Function: nonpayable`

## Inputs

* amount `(Type Of Input: uint256)`
