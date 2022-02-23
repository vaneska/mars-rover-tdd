import { test, expect } from "@playwright/test";

test.describe("add command endpoint", () => {
  test("should return next rover position", async ({ request }) => {
    const addCommandResponse = await request.post(`/command`, {
      data: { command: "RMLM" },
    });

    expect(addCommandResponse.status()).toBe(201);

    const { point } = await addCommandResponse.json();
    const verificationResponse = await request.get(`/budget/${budgetId}`);
    expect(point.x).toBe(1);
    expect(point.y).toBe(1);
  });
});
