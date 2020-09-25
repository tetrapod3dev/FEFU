package com.cloud.domain;

public class OfficialAndPersonalDto {

	private int no;
	private int campaignNo;
	private String mission;
	private String authProcess;
	private String authStartTime;
	private String authEndTime;
	private int headcount;
	private String requirement;

	public int getNo() {
		return no;
	}

	public void setNo(int no) {
		this.no = no;
	}

	public int getCampaignNo() {
		return campaignNo;
	}

	public void setCampaignNo(int campaignNo) {
		this.campaignNo = campaignNo;
	}

	public String getMission() {
		return mission;
	}

	public void setMission(String mission) {
		this.mission = mission;
	}

	public String getAuthProcess() {
		return authProcess;
	}

	public void setAuthProcess(String authProcess) {
		this.authProcess = authProcess;
	}

	public String getAuthStartTime() {
		return authStartTime;
	}

	public void setAuthStartTime(String authStartTime) {
		this.authStartTime = authStartTime;
	}

	public String getAuthEndTime() {
		return authEndTime;
	}

	public void setAuthEndTime(String authEndTime) {
		this.authEndTime = authEndTime;
	}

	public int getHeadcount() {
		return headcount;
	}

	public void setHeadcount(int headcount) {
		this.headcount = headcount;
	}

	public String getRequirement() {
		return requirement;
	}

	public void setRequirement(String requirement) {
		this.requirement = requirement;
	}

}
